---
layout: default
title: Enriching Knowledge Distillation with Cross-Modal Teacher Fusion
---

# Enriching Knowledge Distillation with Cross-Modal Teacher Fusion

**arXiv**: [2511.09286v1](https://arxiv.org/abs/2511.09286) | [PDF](https://arxiv.org/pdf/2511.09286.pdf)

**作者**: Amir M. Mansourian, Amir Mohammad Babaei, Shohreh Kasaei

---

## 💡 一句话要点

**提出RichKD框架，融合CLIP与视觉教师以增强知识蒸馏效果**

**关键词**: `知识蒸馏` `多模态融合` `CLIP模型` `教师融合` `鲁棒性提升`

## 📋 核心要点

1. 多教师知识蒸馏缺乏知识多样性，仅依赖单模态视觉信息
2. 融合CLIP视觉-语言知识与传统教师，使用多提示文本指导
3. 在多个基准测试中优于基线，提升鲁棒性和预测置信度

## 📄 摘要（原文）

> Multi-teacher knowledge distillation (KD), a more effective technique than traditional single-teacher methods, transfers knowledge from expert teachers to a compact student model using logit or feature matching. However, most existing approaches lack knowledge diversity, as they rely solely on unimodal visual information, overlooking the potential of cross-modal representations. In this work, we explore the use of CLIP's vision-language knowledge as a complementary source of supervision for KD, an area that remains largely underexplored. We propose a simple yet effective framework that fuses the logits and features of a conventional teacher with those from CLIP. By incorporating CLIP's multi-prompt textual guidance, the fused supervision captures both dataset-specific and semantically enriched visual cues. Beyond accuracy, analysis shows that the fused teacher yields more confident and reliable predictions, significantly increasing confident-correct cases while reducing confidently wrong ones. Moreover, fusion with CLIP refines the entire logit distribution, producing semantically meaningful probabilities for non-target classes, thereby improving inter-class consistency and distillation quality. Despite its simplicity, the proposed method, Enriching Knowledge Distillation (RichKD), consistently outperforms most existing baselines across multiple benchmarks and exhibits stronger robustness under distribution shifts and input corruptions.

