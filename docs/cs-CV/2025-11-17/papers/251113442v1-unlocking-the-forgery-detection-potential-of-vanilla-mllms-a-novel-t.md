---
layout: default
title: Unlocking the Forgery Detection Potential of Vanilla MLLMs: A Novel Training-Free Pipeline
---

# Unlocking the Forgery Detection Potential of Vanilla MLLMs: A Novel Training-Free Pipeline

**arXiv**: [2511.13442v1](https://arxiv.org/abs/2511.13442) | [PDF](https://arxiv.org/pdf/2511.13442.pdf)

**作者**: Rui Zuo, Qinyue Tong, Zhe-Ming Lu, Ziqian Lu

---

## 💡 一句话要点

**提出Foresee训练免费管道以解决图像伪造检测泛化与解释性问题**

**关键词**: `图像伪造检测` `多模态大语言模型` `训练免费方法` `篡改定位` `泛化能力` `文本解释`

## 📋 核心要点

1. 现有图像伪造检测方法泛化能力差且解释性有限
2. Foresee无需训练，利用类型先验策略和FFD模块释放MLLM潜力
3. 实验显示在多种篡改类型中定位准确且提供丰富文本解释

## 📄 摘要（原文）

> With the rapid advancement of artificial intelligence-generated content (AIGC) technologies, including multimodal large language models (MLLMs) and diffusion models, image generation and manipulation have become remarkably effortless. Existing image forgery detection and localization (IFDL) methods often struggle to generalize across diverse datasets and offer limited interpretability. Nowadays, MLLMs demonstrate strong generalization potential across diverse vision-language tasks, and some studies introduce this capability to IFDL via large-scale training. However, such approaches cost considerable computational resources, while failing to reveal the inherent generalization potential of vanilla MLLMs to address this problem. Inspired by this observation, we propose Foresee, a training-free MLLM-based pipeline tailored for image forgery analysis. It eliminates the need for additional training and enables a lightweight inference process, while surpassing existing MLLM-based methods in both tamper localization accuracy and the richness of textual explanations. Foresee employs a type-prior-driven strategy and utilizes a Flexible Feature Detector (FFD) module to specifically handle copy-move manipulations, thereby effectively unleashing the potential of vanilla MLLMs in the forensic domain. Extensive experiments demonstrate that our approach simultaneously achieves superior localization accuracy and provides more comprehensive textual explanations. Moreover, Foresee exhibits stronger generalization capability, outperforming existing IFDL methods across various tampering types, including copy-move, splicing, removal, local enhancement, deepfake, and AIGC-based editing. The code will be released in the final version.

