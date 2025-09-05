import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def chunk_text(text, max_chars=7000):  # Reduce chunk size
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

def Yt_video_summarizer(url: str, style: str, language: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.6,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["transcript", "style", "language"],
        template="""Summarize the following YouTube transcript in {style} format and respond in {language} language.
        Transcript: {transcript}"""
    )

    if "v=" in url:
        video_id = url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]
    else:
        return "⚠️ Invalid YouTube URL."

    print(f"Extracted Video ID: {video_id}")

    try:
        ytt = YouTubeTranscriptApi()
        try:
            transcript = ytt.fetch(video_id)
        except Exception:
            transcript_list = ytt.list(video_id)
            languages = [t.language_code for t in transcript_list]
            try:
                chosen = transcript_list.find_manually_created_transcript(languages)
            except Exception:
                try:
                    chosen = transcript_list.find_generated_transcript(languages)
                except Exception:
                    chosen = next(iter(transcript_list))
            transcript = chosen.fetch()
        if hasattr(transcript, "to_raw_data"):
            transcript_data = transcript.to_raw_data()
        else:
            transcript_data = transcript
        transcript_text = " ".join(
            entry.get("text", "") for entry in transcript_data if entry.get("text")
        )
        if not transcript_text.strip():
            return "⚠️ Transcript appears empty."
    except Exception as e:
        return f"❌ Error fetching transcript: {e}"

    max_chars = 7000
    chain = LLMChain(llm=llm, prompt=prompt)
    if len(transcript_text) > max_chars:
        chunks = chunk_text(transcript_text, max_chars)
        summaries = []
        for chunk in chunks:
            print("Chunk length:", len(chunk))
            try:
                summary = chain.invoke({"transcript": chunk, "style": style, "language": language})
            except Exception as e:
                summary = f"⚠️ Error during summarization: {e}"
            if isinstance(summary, dict):
                summaries.append(summary.get("text", ""))
            else:
                summaries.append(str(summary))
        combined = " ".join(summaries)
        print("Combined summary length:", len(combined))
        # Truncate combined summary if needed
        max_combined_chars = 10000
        if len(combined) > max_combined_chars:
            combined = combined[:max_combined_chars]
            combined += "\n\n[Summary truncated due to length.]"
        try:
            final_summary = chain.invoke({"transcript": combined, "style": style, "language": language})
        except Exception as e:
            final_summary = f"⚠️ Error during summarization: {e}"
        if isinstance(final_summary, dict):
            return final_summary.get("text", "")
        else:
            return final_summary
    else:
        try:
            result = chain.invoke({"transcript": transcript_text, "style": style, "language": language})
        except Exception as e:
            result = f"⚠️ Error during summarization: {e}"
        if isinstance(result, dict):
            return result.get("text", "")
        else:
            return result

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    summary = Yt_video_summarizer(
        url='https://www.youtube.com/watch?v=hxHiYHJPekM',
        style='In bullet points',
        language='ENGLISH'
    )
    print(summary)