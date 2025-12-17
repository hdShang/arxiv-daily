---
layout: default
title: Optimizing Medical Question-Answering Systems: A Comparative Study of Fine-Tuned and Zero-Shot Large Language Models with RAG Framework
---

# Optimizing Medical Question-Answering Systems: A Comparative Study of Fine-Tuned and Zero-Shot Large Language Models with RAG Framework

**arXiv**: [2512.05863v1](https://arxiv.org/abs/2512.05863) | [PDF](https://arxiv.org/pdf/2512.05863.pdf)

**作者**: Tasnimul Hassan, Md Faisal Karim, Haziq Jeelani, Elham Behnam, Robert Green, Fayeq Jeelani Syed

---

## 💡 一句话要点

**提出基于RAG的医学问答系统，通过检索增强和微调开源LLM提升准确性和减少幻觉。**

**关键词**: `医学问答系统` `检索增强生成` `大型语言模型微调` `LoRA` `PubMedQA` `幻觉减少`

## 📋 核心要点

1. 核心问题：医学问答中LLM存在事实准确性低和幻觉问题，需结合领域知识。
2. 方法要点：使用RAG框架检索医学文献，并基于LoRA微调LLaMA~2和Falcon模型。
3. 实验或效果：在PubMedQA上微调LLaMA~2准确率达71.8%，比零样本基线提升16.4%，幻觉减少约60%。

## 📄 摘要（原文）

> Medical question-answering (QA) systems can benefit from advances in large language models (LLMs), but directly applying LLMs to the clinical domain poses challenges such as maintaining factual accuracy and avoiding hallucinations. In this paper, we present a retrieval-augmented generation (RAG) based medical QA system that combines domain-specific knowledge retrieval with open-source LLMs to answer medical questions. We fine-tune two state-of-the-art open LLMs (LLaMA~2 and Falcon) using Low-Rank Adaptation (LoRA) for efficient domain specialization. The system retrieves relevant medical literature to ground the LLM's answers, thereby improving factual correctness and reducing hallucinations. We evaluate the approach on benchmark datasets (PubMedQA and MedMCQA) and show that retrieval augmentation yields measurable improvements in answer accuracy compared to using LLMs alone. Our fine-tuned LLaMA~2 model achieves 71.8% accuracy on PubMedQA, substantially improving over the 55.4% zero-shot baseline, while maintaining transparency by providing source references. We also detail the system design and fine-tuning methodology, demonstrating that grounding answers in retrieved evidence reduces unsupported content by approximately 60%. These results highlight the potential of RAG-augmented open-source LLMs for reliable biomedical QA, pointing toward practical clinical informatics applications.

