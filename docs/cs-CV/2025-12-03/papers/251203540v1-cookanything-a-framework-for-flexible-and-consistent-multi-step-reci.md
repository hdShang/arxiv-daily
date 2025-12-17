---
layout: default
title: CookAnything: A Framework for Flexible and Consistent Multi-Step Recipe Image Generation
---

# CookAnything: A Framework for Flexible and Consistent Multi-Step Recipe Image Generation

**arXiv**: [2512.03540v1](https://arxiv.org/abs/2512.03540) | [PDF](https://arxiv.org/pdf/2512.03540.pdf)

**作者**: Ruoxuan Zhang, Bin Wen, Hongxia Xie, Yi Yao, Songhan Zuo, Jian-Yu Jiang-Lin, Hong-Han Shuai, Wen-Huang Cheng

---

## 💡 一句话要点

**提出CookAnything框架以解决多步骤食谱图像生成中的灵活性和一致性问题**

**关键词**: `多步骤图像生成` `扩散模型` `食谱插图` `时序连贯性` `成分一致性` `灵活位置编码`

## 📋 核心要点

1. 核心问题：现有扩散模型难以处理结构化多步骤场景，且食谱长度可变性导致图像生成固定数量，缺乏灵活性和一致性。
2. 方法要点：引入Step-wise Regional Control对齐文本步骤与图像区域，Flexible RoPE增强时序连贯性和空间多样性，Cross-Step Consistency Control保持跨步骤成分一致性。
3. 实验或效果：在食谱插图基准测试中优于现有方法，支持任意长度指令的高质量视觉合成，适用于教学媒体和程序内容创建。

## 📄 摘要（原文）

> Cooking is a sequential and visually grounded activity, where each step such as chopping, mixing, or frying carries both procedural logic and visual semantics. While recent diffusion models have shown strong capabilities in text-to-image generation, they struggle to handle structured multi-step scenarios like recipe illustration. Additionally, current recipe illustration methods are unable to adjust to the natural variability in recipe length, generating a fixed number of images regardless of the actual instructions structure. To address these limitations, we present CookAnything, a flexible and consistent diffusion-based framework that generates coherent, semantically distinct image sequences from textual cooking instructions of arbitrary length. The framework introduces three key components: (1) Step-wise Regional Control (SRC), which aligns textual steps with corresponding image regions within a single denoising process; (2) Flexible RoPE, a step-aware positional encoding mechanism that enhances both temporal coherence and spatial diversity; and (3) Cross-Step Consistency Control (CSCC), which maintains fine-grained ingredient consistency across steps. Experimental results on recipe illustration benchmarks show that CookAnything performs better than existing methods in training-based and training-free settings. The proposed framework supports scalable, high-quality visual synthesis of complex multi-step instructions and holds significant potential for broad applications in instructional media, and procedural content creation.

