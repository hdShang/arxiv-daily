---
layout: default
title: Reducing Domain Gap with Diffusion-Based Domain Adaptation for Cell Counting
---

# Reducing Domain Gap with Diffusion-Based Domain Adaptation for Cell Counting

**arXiv**: [2512.11763v1](https://arxiv.org/abs/2512.11763) | [PDF](https://arxiv.org/pdf/2512.11763.pdf)

**作者**: Mohammad Dehghanmanshadi, Wallapak Tavanapong

---

## 💡 一句话要点

**提出基于扩散模型的InST风格迁移方法，以降低细胞计数中合成与真实显微图像的域差距。**

**关键词**: `域适应` `扩散模型` `风格迁移` `细胞计数` `显微图像`

## 📋 核心要点

1. 核心问题：传统域适应方法难以处理合成显微图像缺乏真实纹理和视觉模式的问题。
2. 方法要点：结合潜在空间自适应实例归一化和扩散模型中的随机反转，将真实荧光显微图像风格迁移至合成图像。
3. 实验或效果：在细胞计数任务中，InST合成数据训练模型比硬编码合成数据降低37% MAE，比Cell200-s降低52% MAE。

## 📄 摘要（原文）

> Generating realistic synthetic microscopy images is critical for training deep learning models in label-scarce environments, such as cell counting with many cells per image. However, traditional domain adaptation methods often struggle to bridge the domain gap when synthetic images lack the complex textures and visual patterns of real samples. In this work, we adapt the Inversion-Based Style Transfer (InST) framework originally designed for artistic style transfer to biomedical microscopy images. Our method combines latent-space Adaptive Instance Normalization with stochastic inversion in a diffusion model to transfer the style from real fluorescence microscopy images to synthetic ones, while weakly preserving content structure.
>   We evaluate the effectiveness of our InST-based synthetic dataset for downstream cell counting by pre-training and fine-tuning EfficientNet-B0 models on various data sources, including real data, hard-coded synthetic data, and the public Cell200-s dataset. Models trained with our InST-synthesized images achieve up to 37\% lower Mean Absolute Error (MAE) compared to models trained on hard-coded synthetic data, and a 52\% reduction in MAE compared to models trained on Cell200-s (from 53.70 to 25.95 MAE). Notably, our approach also outperforms models trained on real data alone (25.95 vs. 27.74 MAE). Further improvements are achieved when combining InST-synthesized data with lightweight domain adaptation techniques such as DACS with CutMix. These findings demonstrate that InST-based style transfer most effectively reduces the domain gap between synthetic and real microscopy data. Our approach offers a scalable path for enhancing cell counting performance while minimizing manual labeling effort. The source code and resources are publicly available at: https://github.com/MohammadDehghan/InST-Microscopy.

