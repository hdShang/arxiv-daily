---
layout: default
title: Memory-SAM: Human-Prompt-Free Tongue Segmentation via Retrieval-to-Prompt
---

# Memory-SAM: Human-Prompt-Free Tongue Segmentation via Retrieval-to-Prompt

**arXiv**: [2510.15849v1](https://arxiv.org/abs/2510.15849) | [PDF](https://arxiv.org/pdf/2510.15849.pdf)

**作者**: Joongwon Chae, Lihui Luo, Xi Yuan, Dongmei Yu, Zhenglin Chen, Lian Zhang, Peiwu Qin

---

## 💡 一句话要点

**提出Memory-SAM以自动分割舌象，无需人工提示或训练**

**关键词**: `舌分割` `检索到提示` `训练自由方法` `DINOv3特征` `FAISS检索` `SAM2模型`

## 📋 核心要点

1. 核心问题：舌分割需大量标注数据，SAM模型依赖人工提示。
2. 方法要点：通过检索先例生成点提示，指导SAM2自动分割。
3. 实验效果：在混合测试集上mIoU达0.9863，优于基线方法。

## 📄 摘要（原文）

> Accurate tongue segmentation is crucial for reliable TCM analysis. Supervised
> models require large annotated datasets, while SAM-family models remain
> prompt-driven. We present Memory-SAM, a training-free, human-prompt-free
> pipeline that automatically generates effective prompts from a small memory of
> prior cases via dense DINOv3 features and FAISS retrieval. Given a query image,
> mask-constrained correspondences to the retrieved exemplar are distilled into
> foreground/background point prompts that guide SAM2 without manual clicks or
> model fine-tuning. We evaluate on 600 expert-annotated images (300 controlled,
> 300 in-the-wild). On the mixed test split, Memory-SAM achieves mIoU 0.9863,
> surpassing FCN (0.8188) and a detector-to-box SAM baseline (0.1839). On
> controlled data, ceiling effects above 0.98 make small differences less
> meaningful given annotation variability, while our method shows clear gains
> under real-world conditions. Results indicate that retrieval-to-prompt enables
> data-efficient, robust segmentation of irregular boundaries in tongue imaging.
> The code is publicly available at https://github.com/jw-chae/memory-sam.

