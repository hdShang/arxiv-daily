---
layout: default
title: UniCalli: A Unified Diffusion Framework for Column-Level Generation and Recognition of Chinese Calligraphy
---

# UniCalli: A Unified Diffusion Framework for Column-Level Generation and Recognition of Chinese Calligraphy

**arXiv**: [2510.13745v1](https://arxiv.org/abs/2510.13745) | [PDF](https://arxiv.org/pdf/2510.13745.pdf)

**作者**: Tianshuo Xu, Kai Wang, Zhifei Chen, Leyi Wu, Tianshui Wen, Fei Chao, Ying-Cong Chen

---

## 💡 一句话要点

**提出UniCalli统一扩散框架，解决中文书法列级生成与识别问题**

**关键词**: `中文书法生成` `扩散模型` `联合训练` `列级识别` `古文字处理`

## 📋 核心要点

1. 核心问题：现有方法难以同时保证书法字符正确性和页面美学，如连笔与间距
2. 方法要点：联合训练生成与识别任务，利用不对称噪声和栅格化框图提供空间先验
3. 实验或效果：在8000+数据集上实现生成质量与识别性能提升，并扩展至甲骨文等古文字

## 📄 摘要（原文）

> Computational replication of Chinese calligraphy remains challenging.
> Existing methods falter, either creating high-quality isolated characters while
> ignoring page-level aesthetics like ligatures and spacing, or attempting page
> synthesis at the expense of calligraphic correctness. We introduce
> \textbf{UniCalli}, a unified diffusion framework for column-level recognition
> and generation. Training both tasks jointly is deliberate: recognition
> constrains the generator to preserve character structure, while generation
> provides style and layout priors. This synergy fosters concept-level
> abstractions that improve both tasks, especially in limited-data regimes. We
> curated a dataset of over 8,000 digitized pieces, with ~4,000 densely
> annotated. UniCalli employs asymmetric noising and a rasterized box map for
> spatial priors, trained on a mix of synthetic, labeled, and unlabeled data. The
> model achieves state-of-the-art generative quality with superior ligature
> continuity and layout fidelity, alongside stronger recognition. The framework
> successfully extends to other ancient scripts, including Oracle bone
> inscriptions and Egyptian hieroglyphs. Code and data can be viewed in
> \href{https://github.com/EnVision-Research/UniCalli}{this URL}.

