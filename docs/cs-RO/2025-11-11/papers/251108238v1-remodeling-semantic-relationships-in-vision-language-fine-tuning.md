---
layout: default
title: Remodeling Semantic Relationships in Vision-Language Fine-Tuning
---

# Remodeling Semantic Relationships in Vision-Language Fine-Tuning

**arXiv**: [2511.08238v1](https://arxiv.org/abs/2511.08238) | [PDF](https://arxiv.org/pdf/2511.08238.pdf)

**作者**: Xiangyang Wu, Liu Liu, Baosheng Yu, Jiayan Qiu, Zhenwei Shi

---

## 💡 一句话要点

**提出基于语义关系重塑的方法以改进视觉-语言微调中的多模态对齐**

**关键词**: `视觉-语言微调` `语义关系建模` `多模态对齐` `交叉注意力` `视觉问答` `图像描述生成`

## 📋 核心要点

1. 现有视觉-语言微调方法忽略文本上下文中的语义关系，导致性能不佳
2. 方法包括提取多级视觉语义特征、投影分组相关语义、使用可继承交叉注意力融合特征
3. 在八个基础模型和两个下游任务上评估，优于现有方法

## 📄 摘要（原文）

> Vision-language fine-tuning has emerged as an efficient paradigm for constructing multimodal foundation models. While textual context often highlights semantic relationships within an image, existing fine-tuning methods typically overlook this information when aligning vision and language, thus leading to suboptimal performance. Toward solving this problem, we propose a method that can improve multimodal alignment and fusion based on both semantics and relationships.Specifically, we first extract multilevel semantic features from different vision encoder to capture more visual cues of the relationships. Then, we learn to project the vision features to group related semantics, among which are more likely to have relationships. Finally, we fuse the visual features with the textual by using inheritable cross-attention, where we globally remove the redundant visual relationships by discarding visual-language feature pairs with low correlation. We evaluate our proposed method on eight foundation models and two downstream tasks, visual question answering and image captioning, and show that it outperforms all existing methods.

