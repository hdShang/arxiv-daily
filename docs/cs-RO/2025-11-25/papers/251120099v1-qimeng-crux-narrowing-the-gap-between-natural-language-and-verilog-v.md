---
layout: default
title: QiMeng-CRUX: Narrowing the Gap between Natural Language and Verilog via Core Refined Understanding eXpression
---

# QiMeng-CRUX: Narrowing the Gap between Natural Language and Verilog via Core Refined Understanding eXpression

**arXiv**: [2511.20099v1](https://arxiv.org/abs/2511.20099) | [PDF](https://arxiv.org/pdf/2511.20099.pdf)

**作者**: Lei Huang, Rui Zhang, Jiaming Guo, Yang Zhang, Di Huang, Shuyao Cheng, Pengwei Jin, Chongxiao Li, Zidong Du, Xing Hu, Qi Guo, Yunji Chen

---

## 💡 一句话要点

**提出CRUX结构化中间空间以解决自然语言到Verilog代码生成的模糊性问题**

**关键词**: `硬件描述语言生成` `结构化中间表示` `两阶段训练` `Verilog代码生成` `自然语言处理` `模型优化`

## 📋 核心要点

1. 核心问题：自然语言描述模糊冗余，难以精确生成Verilog代码
2. 方法要点：设计CRUX中间空间和两阶段训练框架，优化语义表达
3. 实验或效果：在多个基准测试中达到最优性能，CRUX可迁移提升其他模型

## 📄 摘要（原文）

> Large language models (LLMs) have shown promising capabilities in hardware description language (HDL) generation. However, existing approaches often rely on free-form natural language descriptions that are often ambiguous, redundant, and unstructured, which poses significant challenges for downstream Verilog code generation. We treat hardware code generation as a complex transformation from an open-ended natural language space to a domain-specific, highly constrained target space. To bridge this gap, we introduce Core Refined Understanding eXpression (CRUX), a structured intermediate space that captures the essential semantics of user intent while organizing the expression for precise Verilog code generation. We further design a two-stage training framework, comprising Joint Expression Modeling and Dual-Space Optimization, to enhance the quality of both CRUX and Verilog code. Experiments across multiple Verilog generation benchmarks demonstrate that our model, CRUX-V, achieves state-of-the-art performance among general models, particularly under challenging design tasks. Furthermore, the CRUX space proves transferable and beneficial when used as input prompts for other code models, highlighting its effectiveness in narrowing the gap between free-form natural language descriptions and precise Verilog generation.

