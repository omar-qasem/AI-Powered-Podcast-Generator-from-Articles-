
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def extract_article_text(url: str) -> str:
    """
    Extracts the main article text from a given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Attempt to find common article content containers
        article_tags = ['article', 'main', 'div', 'p']
        for tag in article_tags:
            content = soup.find(tag, class_=['article-content', 'post-content', 'entry-content', 'story-content'])
            if content:
                return content.get_text(separator='\n', strip=True)
        
        # Fallback: get all paragraph text
        paragraphs = soup.find_all('p')
        return '\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"Error parsing content: {e}"

def summarize_text(text: str) -> str:
    """
    Summarizes the given text using a pre-trained BART model.
    """
    # Using 'facebook/bart-large-cnn' for summarization
    # This model is good for abstractive summarization
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # BART has a maximum input length, typically 1024 tokens. 
    # For longer texts, we might need to split and summarize in chunks.
    # For simplicity, let's assume input text is within limits for now.
    # A more robust solution would involve splitting text into chunks.
    max_chunk_length = 1000  # Approx. tokens for BART
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summaries = []
    for chunk in chunks:
        # Ensure chunk is not empty and has enough content to summarize
        if chunk.strip():
            try:
                summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                print(f"Error summarizing chunk: {e}")
                # If a chunk fails, append the original chunk or a placeholder
                summaries.append(chunk) 
    
    return " ".join(summaries)

def rewrite_to_podcast_style(text: str) -> str:
    """
    Rewrites the text into a conversational, podcast-like tone.
    This will be a placeholder for now, as it requires a more advanced LLM
    or sophisticated prompt engineering that might not be free/offline.
    For initial implementation, we'll use a simple heuristic or a basic prompt.
    """
    # Placeholder: Simple prefix/suffix to make it sound conversational
    # In a real scenario, this would involve a more capable LLM.
    conversational_text = (
        f"Alright, so let's dive into this. What we're essentially looking at is... "
        f"{text.replace('.', '. So, ')}. And that's pretty fascinating, isn't it?"
    )
    return conversational_text

if __name__ == '__main__':
    # Example Usage:
    # For URL extraction
    article_url = "https://www.theverge.com/2024/7/1/24189876/ai-art-copyright-lawsuit-generative-ai-stable-diffusion"
    extracted_text = extract_article_text(article_url)
    print("\n--- Extracted Text ---")
    print(extracted_text[:500]) # Print first 500 chars

    # For summarization
    sample_text = "Artificial intelligence (AI) is rapidly transforming various industries, from healthcare to finance. Its ability to process vast amounts of data and identify patterns has led to breakthroughs in drug discovery, personalized medicine, and fraud detection. However, the ethical implications of AI, such as bias in algorithms and job displacement, are critical concerns that need to be addressed as the technology continues to evolve."
    summary = summarize_text(sample_text)
    print("\n--- Summary ---")
    print(summary)

    # For rewriting
    podcast_summary = rewrite_to_podcast_style(summary)
    print("\n--- Podcast Style ---")
    print(podcast_summary)

    # Test with a longer text for summarization chunking
    long_text = """Artificial intelligence (AI) is rapidly transforming various industries, from healthcare to finance. Its ability to process vast amounts of data and identify patterns has led to breakthroughs in drug discovery, personalized medicine, and fraud detection. However, the ethical implications of AI, such as bias in algorithms and job displacement, are critical concerns that need to be addressed as the technology continues to evolve. The development of AI has been a long journey, starting from early symbolic AI systems to the current era of deep learning. Neural networks, inspired by the human brain, have enabled AI to achieve remarkable feats in image recognition, natural language processing, and game playing. Companies like Google, OpenAI, and Microsoft are at the forefront of AI research, investing heavily in developing more powerful and versatile AI models. The future of AI holds immense promise, with potential applications in autonomous vehicles, smart cities, and advanced robotics. Yet, careful consideration of its societal impact and responsible development practices are paramount to ensure that AI benefits all of humanity. The integration of AI into daily life is becoming increasingly seamless, with AI-powered assistants, recommendation systems, and predictive analytics becoming commonplace. As AI systems become more sophisticated, they will require robust regulatory frameworks and public discourse to navigate the complex challenges they present. Education and retraining initiatives will be crucial to prepare the workforce for the changes brought about by AI, fostering a collaborative environment between humans and intelligent machines. The ongoing research into explainable AI (XAI) aims to make AI decisions more transparent and understandable, building trust and facilitating broader adoption. Furthermore, the concept of artificial general intelligence (AGI), where AI can perform any intellectual task that a human can, remains a long-term goal, with significant research and ethical hurdles to overcome. The global competition in AI development is intense, with nations vying for leadership in this transformative technology. International cooperation will be essential to establish common standards and address global challenges related to AI, ensuring its responsible and equitable deployment across the world. The continuous advancements in computational power and data availability are fueling the rapid progress in AI, pushing the boundaries of what is possible. The interdisciplinary nature of AI research, combining computer science, cognitive science, mathematics, and philosophy, highlights the complexity and breadth of this field. As AI continues to evolve, it will undoubtedly reshape our world in profound ways, making it imperative to approach its development with foresight and a commitment to human well-being."""
    long_summary = summarize_text(long_text)
    print("\n--- Long Text Summary ---")
    print(long_summary)

    podcast_long_summary = rewrite_to_podcast_style(long_summary)
    print("\n--- Long Text Podcast Style ---")
    print(podcast_long_summary)

    # Test with a non-existent URL
    bad_url = "https://this-url-does-not-exist-12345.com"
    bad_url_text = extract_article_text(bad_url)
    print("\n--- Bad URL Test ---")
    print(bad_url_text)



