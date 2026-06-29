# Common Errors Cheat Sheet, the unblocking kit

You will hit errors. That is normal, and recovering calmly is part of the lesson. The AI wrote
the code; the AI can fix it. Before anything, run the **self-rescue protocol**:

1. **Read the last line of the error out loud.** It usually names the problem.
2. **Paste the whole traceback back to the AI** with: *"this errored, fix it and tell me what
   went wrong."*
3. **Stuck after two tries?** Flag the instructor and look at your partner's screen meanwhile.
   (Helping a partner read an error is not backseat driving.)

Below are the 6–8 errors a non-coder actually hits in Colab. Each has what it looks like, what
causes it, and the **exact phrase to paste back to the AI**.

---

**1. Blank or missing API key**
*Looks like:* `PermissionDenied: 400 API key not valid` or `... API_KEY_INVALID`, or your key
variable is empty.
*Cause:* The Gemini key isn't in Colab Secrets, the toggle next to it is off, or the name
doesn't match what the code reads (`GEMINI_API_KEY`).
*Paste back:* "My Gemini API key isn't being found. Show me how to load it from Colab Secrets
named GEMINI_API_KEY and check it's enabled for this notebook."

**2. Rate limit / quota exceeded**
*Looks like:* `429 ResourceExhausted` or `Quota exceeded for quota metric ... per day`.
*Cause:* Too many requests too fast, or you hit the free-tier daily cap.
*Paste back:* "I got a 429 rate-limit error. Add a short retry-with-backoff and a small delay
between calls, and process my data in smaller batches."

**3. Wrong file path / file not uploaded**
*Looks like:* `FileNotFoundError: [Errno 2] No such file or directory: 'mydata.csv'`.
*Cause:* The file isn't uploaded to this Colab session (uploads vanish when the runtime
disconnects), or the path/name is wrong.
*Paste back:* "FileNotFoundError on my data file. Show me how to upload it to this Colab session
and use the correct path."

**4. Empty dataframe (the selector matched nothing)**
*Looks like:* No error, but `len(df) == 0`, or `KeyError` on a column that "should" be there.
*Cause:* The scrape/API call returned nothing, or the parser matched the wrong part of the page.
*Paste back:* "My dataframe is empty after loading. Print the raw response first so we can see
what actually came back, then fix the parsing."

**5. ModuleNotFoundError (package not installed / wrong name)**
*Looks like:* `ModuleNotFoundError: No module named 'sentence_transformers'`.
*Cause:* The install cell wasn't run this session, or the import name differs from the install
name (e.g. install `sentence-transformers`, import `sentence_transformers`).
*Paste back:* "ModuleNotFoundError for X. Give me the exact %pip install line, then the correct
import statement."

**6. Malformed AI output (asked for JSON, got prose)**
*Looks like:* `JSONDecodeError: Expecting value: line 1 column 1`.
*Cause:* The model wrapped its answer in explanation or markdown fences instead of returning
clean JSON.
*Paste back:* "The model returned text around the JSON so parsing failed. Make the prompt demand
JSON only, and strip any code fences before parsing."

**7. Runtime disconnected / out of memory**
*Looks like:* "Your session crashed after using all available RAM," or the runtime reconnects
and your variables are gone.
*Cause:* Too much data in memory at once, or an idle timeout.
*Paste back:* "Colab ran out of memory. Rewrite this to process my data in batches instead of
all at once, and free memory between batches."

**8. GPU not available**
*Looks like:* `RuntimeError: CUDA ... no GPU`, or embeddings run very slowly.
*Cause:* No GPU attached to this runtime.
*Fix yourself:* `Runtime → Change runtime type → T4 GPU`, then re-run. *Paste back if it
persists:* "No GPU is available. Make this run on CPU with a smaller sample so it still
finishes."

---

*Keep this open in a tab during every lab. The move is never to panic. It's to read the last
line, paste it back, and keep moving.*
