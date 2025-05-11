# Day 3: Building a Tool-Calling Agent with Haystack

Today, I completed the Haystack tutorial on creating a tool-calling agent using the `Agent` component and external tools.

### ✅ What I Learned

- How to use `Agent`, `OpenAIChatGenerator`, and `ComponentTool` to build an intelligent assistant.
- Integrated `SerperDevWebSearch` to fetch search engine results.
- Explored `exit_conditions`, `system_prompt`, `streaming_callback`, and other Agent parameters.
- Used `SuperComponent` and `Pipeline` to enable complex tool behavior.
- Built a complete tool-calling pipeline:
  - Web search using SerperDev
  - Fetching and converting HTML content
  - Formatting context for the agent using `ChatPromptBuilder`
- Implemented a research assistant Agent that answers queries with citations in markdown format.

### 🔧 Tools & Libraries Used

- Haystack components: `Agent`, `ComponentTool`, `SuperComponent`, `OpenAIChatGenerator`
- External services: OpenAI API, SerperDev API
- Python packages: `haystack-ai`, `docstring-parser`, `trafilatura`

### 🧠 Key Takeaway

Using Haystack’s `Agent` and tool abstraction, it’s possible to build a multi-step, LLM-powered assistant that can search the web, parse content, and return comprehensive, well-cited answers. 

### Things to Know 
AI 

---

