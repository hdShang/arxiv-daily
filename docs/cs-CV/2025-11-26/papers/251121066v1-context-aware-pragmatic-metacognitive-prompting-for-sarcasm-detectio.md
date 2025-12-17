---
layout: default
title: Context-Aware Pragmatic Metacognitive Prompting for Sarcasm Detection
---

# Context-Aware Pragmatic Metacognitive Prompting for Sarcasm Detection

**arXiv**: [2511.21066v1](https://arxiv.org/abs/2511.21066) | [PDF](https://arxiv.org/pdf/2511.21066.pdf)

**作者**: Michael Iskandardinata, William Christian, Derwin Suhartono

---

## 💡 一句话要点

**提出上下文感知实用元认知提示方法，以提升大语言模型在讽刺检测中的性能。**

**关键词**: `讽刺检测` `大语言模型` `上下文检索` `实用元认知提示` `自然语言处理`

## 📋 核心要点

1. 讽刺检测因语言多样性和文化差异而具挑战性，现有模型对未知词汇检测不可靠。
2. 方法结合检索上下文信息，包括网络检索和模型自知识策略，增强背景理解。
3. 实验在多个数据集上验证，非参数检索显著提升性能，最高达9.87%宏F1改进。

## 📄 摘要（原文）

> Detecting sarcasm remains a challenging task in the areas of Natural Language Processing (NLP) despite recent advances in neural network approaches. Currently, Pre-trained Language Models (PLMs) and Large Language Models (LLMs) are the preferred approach for sarcasm detection. However, the complexity of sarcastic text, combined with linguistic diversity and cultural variation across communities, has made the task more difficult even for PLMs and LLMs. Beyond that, those models also exhibit unreliable detection of words or tokens that require extra grounding for analysis. Building on a state-of-the-art prompting method in LLMs for sarcasm detection called Pragmatic Metacognitive Prompting (PMP), we introduce a retrieval-aware approach that incorporates retrieved contextual information for each target text. Our pipeline explores two complementary ways to provide context: adding non-parametric knowledge using web-based retrieval when the model lacks necessary background, and eliciting the model's own internal knowledge for a self-knowledge awareness strategy. We evaluated our approach with three datasets, such as Twitter Indonesia Sarcastic, SemEval-2018 Task 3, and MUStARD. Non-parametric retrieval resulted in a significant 9.87% macro-F1 improvement on Twitter Indonesia Sarcastic compared to the original PMP method. Self-knowledge retrieval improves macro-F1 by 3.29% on Semeval and by 4.08% on MUStARD. These findings highlight the importance of context in enhancing LLMs performance in sarcasm detection task, particularly the involvement of culturally specific slang, references, or unknown terms to the LLMs. Future work will focus on optimizing the retrieval of relevant contextual information and examining how retrieval quality affects performance. The experiment code is available at: https://github.com/wllchrst/sarcasm-detection_pmp_knowledge-base.

