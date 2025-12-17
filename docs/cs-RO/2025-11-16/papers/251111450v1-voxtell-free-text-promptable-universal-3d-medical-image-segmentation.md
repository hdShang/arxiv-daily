---
layout: default
title: VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation
---

# VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation

**arXiv**: [2511.11450v1](https://arxiv.org/abs/2511.11450) | [PDF](https://arxiv.org/pdf/2511.11450.pdf)

**作者**: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, Klaus Maier-Hein

---

## 💡 一句话要点

**提出VoxTell模型，通过自由文本提示实现通用3D医学图像分割**

**关键词**: `3D医学图像分割` `视觉语言模型` `零样本学习` `多模态融合` `自由文本提示`

## 📋 核心要点

1. 核心问题：医学图像分割需从自由文本描述生成3D掩码，支持多模态和未见类别
2. 方法要点：采用多阶段视觉语言融合，在解码器层对齐文本和视觉特征
3. 实验或效果：在零样本分割中达到SOTA，跨模态泛化强，鲁棒于语言变化

## 📄 摘要（原文）

> We introduce VoxTell, a vision-language model for text-prompted volumetric medical image segmentation. It maps free-form descriptions, from single words to full clinical sentences, to 3D masks. Trained on 62K+ CT, MRI, and PET volumes spanning over 1K anatomical and pathological classes, VoxTell uses multi-stage vision-language fusion across decoder layers to align textual and visual features at multiple scales. It achieves state-of-the-art zero-shot performance across modalities on unseen datasets, excelling on familiar concepts while generalizing to related unseen classes. Extensive experiments further demonstrate strong cross-modality transfer, robustness to linguistic variations and clinical language, as well as accurate instance-specific segmentation from real-world text. Code is available at: https://www.github.com/MIC-DKFZ/VoxTell

