---
layout: default
title: DiffSeg30k: A Multi-Turn Diffusion Editing Benchmark for Localized AIGC Detection
---

# DiffSeg30k: A Multi-Turn Diffusion Editing Benchmark for Localized AIGC Detection

**arXiv**: [2511.19111v1](https://arxiv.org/abs/2511.19111) | [PDF](https://arxiv.org/pdf/2511.19111.pdf)

**作者**: Hai Ci, Ziheng Peng, Pei Yang, Yingxin Xuan, Mike Zheng Shou

---

## 💡 一句话要点

**提出DiffSeg30k数据集以解决扩散编辑局部化检测的基准缺失问题**

**关键词**: `扩散编辑检测` `语义分割基准` `像素级标注` `多轮编辑` `AIGC检测` `跨生成器泛化`

## 📋 核心要点

1. 核心问题：现有AIGC检测基准忽略扩散编辑的局部化，难以应对真实编辑场景。
2. 方法要点：构建30k扩散编辑图像数据集，含像素级标注、多轮编辑和多样化模型。
3. 实验或效果：基准测试显示分割方法在局部化检测中具挑战，但整体分类性能优越。

## 📄 摘要（原文）

> Diffusion-based editing enables realistic modification of local image regions, making AI-generated content harder to detect. Existing AIGC detection benchmarks focus on classifying entire images, overlooking the localization of diffusion-based edits. We introduce DiffSeg30k, a publicly available dataset of 30k diffusion-edited images with pixel-level annotations, designed to support fine-grained detection. DiffSeg30k features: 1) In-the-wild images--we collect images or image prompts from COCO to reflect real-world content diversity; 2) Diverse diffusion models--local edits using eight SOTA diffusion models; 3) Multi-turn editing--each image undergoes up to three sequential edits to mimic real-world sequential editing; and 4) Realistic editing scenarios--a vision-language model (VLM)-based pipeline automatically identifies meaningful regions and generates context-aware prompts covering additions, removals, and attribute changes. DiffSeg30k shifts AIGC detection from binary classification to semantic segmentation, enabling simultaneous localization of edits and identification of the editing models. We benchmark three baseline segmentation approaches, revealing significant challenges in semantic segmentation tasks, particularly concerning robustness to image distortions. Experiments also reveal that segmentation models, despite being trained for pixel-level localization, emerge as highly reliable whole-image classifiers of diffusion edits, outperforming established forgery classifiers while showing great potential in cross-generator generalization. We believe DiffSeg30k will advance research in fine-grained localization of AI-generated content by demonstrating the promise and limitations of segmentation-based methods. DiffSeg30k is released at: https://huggingface.co/datasets/Chaos2629/Diffseg30k

