---
layout: default
title: ManipShield: A Unified Framework for Image Manipulation Detection, Localization and Explanation
---

# ManipShield: A Unified Framework for Image Manipulation Detection, Localization and Explanation

**arXiv**: [2511.14259v1](https://arxiv.org/abs/2511.14259) | [PDF](https://arxiv.org/pdf/2511.14259.pdf)

**作者**: Zitong Xu, Huiyu Duan, Xiaoyu Wang, Zhaolin Cai, Kaiwei Zhang, Qiang Hu, Jing Liu, Xiongkuo Min, Guangtao Zhai

---

## 💡 一句话要点

**提出ManipShield框架以解决AI编辑图像检测、定位和解释的挑战**

**关键词**: `图像操纵检测` `多模态大语言模型` `基准数据集` `解释性AI` `对比学习微调`

## 📋 核心要点

1. 核心问题：生成模型导致图像操纵多样且逼真，现有检测方法泛化性和解释性不足
2. 方法要点：基于多模态大语言模型，结合对比LoRA微调和任务特定解码器实现统一检测
3. 实验或效果：在ManipBench和公共数据集上达到先进性能，展示强泛化能力

## 📄 摘要（原文）

> With the rapid advancement of generative models, powerful image editing methods now enable diverse and highly realistic image manipulations that far surpass traditional deepfake techniques, posing new challenges for manipulation detection. Existing image manipulation detection and localization (IMDL) benchmarks suffer from limited content diversity, narrow generative-model coverage, and insufficient interpretability, which hinders the generalization and explanation capabilities of current manipulation detection methods. To address these limitations, we introduce \textbf{ManipBench}, a large-scale benchmark for image manipulation detection and localization focusing on AI-edited images. ManipBench contains over 450K manipulated images produced by 25 state-of-the-art image editing models across 12 manipulation categories, among which 100K images are further annotated with bounding boxes, judgment cues, and textual explanations to support interpretable detection. Building upon ManipBench, we propose \textbf{ManipShield}, an all-in-one model based on a Multimodal Large Language Model (MLLM) that leverages contrastive LoRA fine-tuning and task-specific decoders to achieve unified image manipulation detection, localization, and explanation. Extensive experiments on ManipBench and several public datasets demonstrate that ManipShield achieves state-of-the-art performance and exhibits strong generality to unseen manipulation models. Both ManipBench and ManipShield will be released upon publication.

