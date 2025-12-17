---
layout: default
title: Malicious Image Analysis via Vision-Language Segmentation Fusion: Detection, Element, and Location in One-shot
---

# Malicious Image Analysis via Vision-Language Segmentation Fusion: Detection, Element, and Location in One-shot

**arXiv**: [2512.04599v1](https://arxiv.org/abs/2512.04599) | [PDF](https://arxiv.org/pdf/2512.04599.pdf)

**作者**: Sheng Hang, Chaoxiang He, Hongsheng Hu, Hanqing Hu, Bin Benjamin Zhu, Shi-Feng Sun, Dawu Gu, Shuo Wang

---

## 💡 一句话要点

**提出零次学习视觉-语言分割融合方法，实现恶意图像检测、元素识别与定位一体化**

**关键词**: `恶意图像检测` `视觉-语言融合` `零次学习` `像素级定位` `对抗鲁棒性` `开放词汇提示`

## 📋 核心要点

1. 核心问题：恶意图像检测需超越图像级标签，实现元素级识别与像素级定位
2. 方法要点：融合基础分割模型与视觉语言模型，通过开放词汇提示评分并加权融合生成恶意对象图
3. 实验或效果：在790张图像数据集上达到85.8%元素级召回率，对抗攻击下性能下降不超过10%

## 📄 摘要（原文）

> Detecting illicit visual content demands more than image-level NSFW flags; moderators must also know what objects make an image illegal and where those objects occur. We introduce a zero-shot pipeline that simultaneously (i) detects if an image contains harmful content, (ii) identifies each critical element involved, and (iii) localizes those elements with pixel-accurate masks - all in one pass. The system first applies foundation segmentation model (SAM) to generate candidate object masks and refines them into larger independent regions. Each region is scored for malicious relevance by a vision-language model using open-vocabulary prompts; these scores weight a fusion step that produces a consolidated malicious object map. An ensemble across multiple segmenters hardens the pipeline against adaptive attacks that target any single segmentation method. Evaluated on a newly-annotated 790-image dataset spanning drug, sexual, violent and extremist content, our method attains 85.8% element-level recall, 78.1% precision and a 92.1% segment-success rate - exceeding direct zero-shot VLM localization by 27.4% recall at comparable precision. Against PGD adversarial perturbations crafted to break SAM and VLM, our method's precision and recall decreased by no more than 10%, demonstrating high robustness against attacks. The full pipeline processes an image in seconds, plugs seamlessly into existing VLM workflows, and constitutes the first practical tool for fine-grained, explainable malicious-image moderation.

