---
layout: default
title: GenColorBench: A Color Evaluation Benchmark for Text-to-Image Generation Models
---

# GenColorBench: A Color Evaluation Benchmark for Text-to-Image Generation Models

**arXiv**: [2510.20586v1](https://arxiv.org/abs/2510.20586) | [PDF](https://arxiv.org/pdf/2510.20586.pdf)

**作者**: Muhammad Atif Butt, Alexandra Gomez-Villa, Tao Wu, Javier Vazquez-Corral, Joost Van De Weijer, Kai Wang

---

## 💡 一句话要点

**提出GenColorBench以评估文本到图像生成模型的颜色精度**

**关键词**: `文本到图像生成` `颜色评估基准` `颜色可控性` `感知评估` `自动化评估`

## 📋 核心要点

1. 现有文本到图像模型在细粒度颜色可控性上表现不佳，缺乏系统评估
2. 基于ISCC-NBS和CSS3/X11颜色系统，构建包含44K提示的基准，支持数值颜色
3. 评估显示模型性能差异，识别失败模式，指导颜色生成改进

## 📄 摘要（原文）

> Recent years have seen impressive advances in text-to-image generation, with
> image generative or unified models producing high-quality images from text. Yet
> these models still struggle with fine-grained color controllability, often
> failing to accurately match colors specified in text prompts. While existing
> benchmarks evaluate compositional reasoning and prompt adherence, none
> systematically assess color precision. Color is fundamental to human visual
> perception and communication, critical for applications from art to design
> workflows requiring brand consistency. However, current benchmarks either
> neglect color or rely on coarse assessments, missing key capabilities such as
> interpreting RGB values or aligning with human expectations. To this end, we
> propose GenColorBench, the first comprehensive benchmark for text-to-image
> color generation, grounded in color systems like ISCC-NBS and CSS3/X11,
> including numerical colors which are absent elsewhere. With 44K color-focused
> prompts covering 400+ colors, it reveals models' true capabilities via
> perceptual and automated assessments. Evaluations of popular text-to-image
> models using GenColorBench show performance variations, highlighting which
> color conventions models understand best and identifying failure modes. Our
> GenColorBench assessments will guide improvements in precise color generation.
> The benchmark will be made public upon acceptance.

