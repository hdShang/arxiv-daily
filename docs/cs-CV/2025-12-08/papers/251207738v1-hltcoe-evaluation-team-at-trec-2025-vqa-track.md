---
layout: default
title: HLTCOE Evaluation Team at TREC 2025: VQA Track
---

# HLTCOE Evaluation Team at TREC 2025: VQA Track

**arXiv**: [2512.07738v1](https://arxiv.org/abs/2512.07738) | [PDF](https://arxiv.org/pdf/2512.07738.pdf)

**作者**: Dengjia Zhang, Charles Weng, Katherine Guerrerio, Yi Lu, Kenton Murray, Alexander Martin, Reno Kriz, Benjamin Van Durme

---

## 💡 一句话要点

**提出基于列表学习框架的视频问答方法，通过候选答案重排序提升语义精度和排序一致性**

**关键词**: `视频问答` `列表学习` `答案重排序` `多模态模型` `时序推理`

## 📋 核心要点

1. 针对视频问答的答案生成任务，核心问题是提升答案的语义精度和排序稳定性
2. 方法采用列表学习框架，先由基础多模态模型生成候选答案，再用带掩码指针交叉熵损失和排序权重的模型进行重排序
3. 实验表明该方法在准确性和排序稳定性上取得一致提升，尤其在需要时序推理和语义消歧的问题上效果显著

## 📄 摘要（原文）

> The HLTCOE Evaluation team participated in TREC VQA's Answer Generation (AG) task, for which we developed a listwise learning framework that aims to improve semantic precision and ranking consistency in answer generation. Given a video-question pair, a base multimodal model first generates multiple candidate answers, which are then reranked using a model trained with a novel Masked Pointer Cross-Entropy Loss with Rank Weights. This objective integrates pointer-based candidate selection, rank-dependent weighting, and masked cross-entropy under vocabulary restriction, enabling stable and interpretable listwise optimization. By bridging generative modeling with discriminative ranking, our method produces coherent, fine-grained answer lists. Experiments reveal consistent gains in accuracy and ranking stability, especially for questions requiring temporal reasoning and semantic disambiguation.

