---
layout: default
title: MultiBanana: A Challenging Benchmark for Multi-Reference Text-to-Image Generation
---

# MultiBanana: A Challenging Benchmark for Multi-Reference Text-to-Image Generation

**arXiv**: [2511.22989v1](https://arxiv.org/abs/2511.22989) | [PDF](https://arxiv.org/pdf/2511.22989.pdf)

**作者**: Yuta Oshima, Daiki Miyake, Kohsei Matsutani, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta

---

## 💡 一句话要点

**提出MultiBanana基准以评估多参考文本到图像生成模型的性能与局限**

**关键词**: `多参考图像生成` `基准数据集` `文本到图像模型` `模型评估` `图像编辑` `多语言生成`

## 📋 核心要点

1. 现有基准数据集多关注单参考或少数参考图像生成，难以全面衡量多参考条件下的模型进展
2. MultiBanana通过设计五个多参考特定问题维度，如参考数量变化、领域不匹配和罕见概念，系统评估模型能力
3. 分析多种模型揭示其优势、典型失败模式和改进方向，并作为开放基准促进公平比较

## 📄 摘要（原文）

> Recent text-to-image generation models have acquired the ability of multi-reference generation and editing; the ability to inherit the appearance of subjects from multiple reference images and re-render them under new contexts. However, the existing benchmark datasets often focus on the generation with single or a few reference images, which prevents us from measuring the progress on how model performance advances or pointing out their weaknesses, under different multi-reference conditions. In addition, their task definitions are still vague, typically limited to axes such as "what to edit" or "how many references are given", and therefore fail to capture the intrinsic difficulty of multi-reference settings. To address this gap, we introduce $\textbf{MultiBanana}$, which is carefully designed to assesses the edge of model capabilities by widely covering multi-reference-specific problems at scale: (1) varying the number of references, (2) domain mismatch among references (e.g., photo vs. anime), (3) scale mismatch between reference and target scenes, (4) references containing rare concepts (e.g., a red banana), and (5) multilingual textual references for rendering. Our analysis among a variety of text-to-image models reveals their superior performances, typical failure modes, and areas for improvement. MultiBanana will be released as an open benchmark to push the boundaries and establish a standardized basis for fair comparison in multi-reference image generation. Our data and code are available at https://github.com/matsuolab/multibanana .

