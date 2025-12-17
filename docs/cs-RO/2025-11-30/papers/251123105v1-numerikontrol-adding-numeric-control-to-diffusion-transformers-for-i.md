---
layout: default
title: NumeriKontrol: Adding Numeric Control to Diffusion Transformers for Instruction-based Image Editing
---

# NumeriKontrol: Adding Numeric Control to Diffusion Transformers for Instruction-based Image Editing

**arXiv**: [2511.23105v1](https://arxiv.org/abs/2511.23105) | [PDF](https://arxiv.org/pdf/2511.23105.pdf)

**作者**: Zhenyu Xu, Xiaoqi Shen, Haotian Nan, Xinyu Zhang

---

## 💡 一句话要点

**提出NumeriKontrol框架，通过数值适配器为扩散变换器添加数值控制，以解决基于指令的图像编辑中编辑强度精细控制不足的问题。**

**关键词**: `指令式图像编辑` `扩散变换器` `数值控制` `零样本编辑` `属性变换数据集`

## 📋 核心要点

1. 核心问题：基于文本指令的图像编辑缺乏对编辑强度的精确控制，难以实现细粒度调整。
2. 方法要点：引入数值适配器编码连续标量值，以即插即用方式注入扩散模型，支持零样本多条件编辑。
3. 实验或效果：在多样化属性编辑场景中实现准确、连续且稳定的尺度控制，提升用户可控性。

## 📄 摘要（原文）

> Instruction-based image editing enables intuitive manipulation through natural language commands. However, text instructions alone often lack the precision required for fine-grained control over edit intensity. We introduce NumeriKontrol, a framework that allows users to precisely adjust image attributes using continuous scalar values with common units. NumeriKontrol encodes numeric editing scales via an effective Numeric Adapter and injects them into diffusion models in a plug-and-play manner. Thanks to a task-separated design, our approach supports zero-shot multi-condition editing, allowing users to specify multiple instructions in any order. To provide high-quality supervision, we synthesize precise training data from reliable sources, including high-fidelity rendering engines and DSLR cameras. Our Common Attribute Transform (CAT) dataset covers diverse attribute manipulations with accurate ground-truth scales, enabling NumeriKontrol to function as a simple yet powerful interactive editing studio. Extensive experiments show that NumeriKontrol delivers accurate, continuous, and stable scale control across a wide range of attribute editing scenarios. These contributions advance instruction-based image editing by enabling precise, scalable, and user-controllable image manipulation.

