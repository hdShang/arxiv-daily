---
layout: default
title: Tourism Question Answer System in Indian Language using Domain-Adapted Foundation Models
---

# Tourism Question Answer System in Indian Language using Domain-Adapted Foundation Models

**arXiv**: [2511.23235v1](https://arxiv.org/abs/2511.23235) | [PDF](https://arxiv.org/pdf/2511.23235.pdf)

**作者**: Praveen Gatla, Anushka, Nikita Kanwar, Gouri Sahoo, Rajesh Kumar Mundotiya

---

## 💡 一句话要点

**提出基于领域适应基础模型的印地语旅游问答系统，以解决文化特定场景下低资源QA问题。**

**关键词**: `印地语问答系统` `旅游领域适应` `基础模型微调` `低秩适应` `文化特定NLP` `低资源数据集`

## 📋 核心要点

1. 核心问题：缺乏针对印地语旅游领域（如瓦拉纳西文化）的问答数据集和资源，影响文化细微应用。
2. 方法要点：构建并增强印地语QA数据集，使用BERT和RoBERTa基础模型，通过SFT和LoRA微调优化参数效率和性能。
3. 实验或效果：LoRA微调在F1达85.3%的同时减少98%可训练参数，RoBERTa在捕捉文化术语（如Aarti）方面表现更优。

## 📄 摘要（原文）

> This article presents the first comprehensive study on designing a baseline extractive question-answering (QA) system for the Hindi tourism domain, with a specialized focus on the Varanasi-a cultural and spiritual hub renowned for its Bhakti-Bhaav (devotional ethos). Targeting ten tourism-centric subdomains-Ganga Aarti, Cruise, Food Court, Public Toilet, Kund, Museum, General, Ashram, Temple and Travel, the work addresses the absence of language-specific QA resources in Hindi for culturally nuanced applications. In this paper, a dataset comprising 7,715 Hindi QA pairs pertaining to Varanasi tourism was constructed and subsequently augmented with 27,455 pairs generated via Llama zero-shot prompting. We propose a framework leveraging foundation models-BERT and RoBERTa, fine-tuned using Supervised Fine-Tuning (SFT) and Low-Rank Adaptation (LoRA), to optimize parameter efficiency and task performance. Multiple variants of BERT, including pre-trained languages (e.g., Hindi-BERT), are evaluated to assess their suitability for low-resource domain-specific QA. Evaluation metrics - F1, BLEU, and ROUGE-L - highlight trade-offs between answer precision and linguistic fluency. Experiments demonstrate that LoRA-based fine-tuning achieves competitive performance (85.3\% F1) while reducing trainable parameters by 98\% compared to SFT, striking a balance between efficiency and accuracy. Comparative analysis across models reveals that RoBERTa with SFT outperforms BERT variants in capturing contextual nuances, particularly for culturally embedded terms (e.g., Aarti, Kund). This work establishes a foundational baseline for Hindi tourism QA systems, emphasizing the role of LORA in low-resource settings and underscoring the need for culturally contextualized NLP frameworks in the tourism domain.

