                          [Graph Image]
                                ↓
                        +-----------------+
                        |   VLM Loader    |  ← (load & preprocess image)
                        +--------+--------+
                                 ↓
              +----------------------------------------+
              |   Reasoning Agents (Gemini Models)     |
              +----------------------------------------+
                ↓          ↓            ↓          ↓
        Hamilton     Node Count     Edge Count   Planarity
                ↓          ↓            ↓          ↓
              +----------------------------------------+
              |         Planner / Aggregator           |
              +----------------+-----------------------+
                               ↓
                     +--------------------+
                     |  Narrator (LLM)    |
                     +--------------------+
                               ↓
                     [Final Explanation]
