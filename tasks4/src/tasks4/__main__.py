from openai import OpenAI

# ---- CONFIG ----
MODEL = "gpt-5-mini"  # Chat Completions model
client = OpenAI()

# ---- SAMPLE PARAGRAPH-LENGTH DESCRIPTIONS ----
descriptions = [
    """
    Develop a workflow automation pipeline that ingests CSV files,
    validates the data for missing fields, transforms it into a normalized format,
    and then loads it into a PostgreSQL database. Ensure that errors are logged and
    that the system can be rerun idempotently without duplicating records.
    """,
    """
    Build a web-based dashboard for monitoring real-time server metrics.
    The dashboard should visualize CPU usage, memory consumption, request throughput,
    and error rates. It should refresh every 5 seconds and allow administrators to
    filter by server or time range.
    """
]

# ---- FUNCTION TO SUMMARIZE A PARAGRAPH USING CHAT COMPLETIONS ----
def summarize_task(text: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You summarize tasks into short, 3–6 word phrases."
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        max_tokens=20,
    )
    return response.choices[0].message.content.strip()

# ---- MAIN LOOP ----
def main():
    print("Summaries:\n")
    for i, description in enumerate(descriptions, start=1):
        summary = summarize_task(description)
        print(f"{i}. {summary}")

if __name__ == "__main__":
    main()
