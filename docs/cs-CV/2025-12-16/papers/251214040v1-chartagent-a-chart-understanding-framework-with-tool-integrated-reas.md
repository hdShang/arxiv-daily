---
layout: default
title: ChartAgent: A Chart Understanding Framework with Tool Integrated Reasoning
---

# ChartAgent: A Chart Understanding Framework with Tool Integrated Reasoning

**arXiv**: [2512.14040v1](https://arxiv.org/abs/2512.14040) | [PDF](https://arxiv.org/pdf/2512.14040.pdf)

**作者**: Boran Wang, Xinming Wang, Yi Chen, Xiang Li, Jian Xu, Jing Yuan, Chenglin Liu

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ChartAgent框架，通过工具集成推理解决图表理解在稀疏标注下的鲁棒性问题。**

**关键词**: `图表理解` `工具集成推理` `多模态大语言模型` `稀疏标注鲁棒性` `结构化证据包` `视觉解析` `可扩展框架` `自动化分析`

## 📋 核心要点

1. 现有MLLMs依赖显式文本标注，关键数字缺失时性能显著下降，限制了实际应用。
2. 提出ChartAgent框架，基于工具集成推理，将图表分析分解为可观察步骤，动态编排模块化工具库。
3. 实验显示，ChartAgent在稀疏标注设置下大幅提升鲁棒性，提供可追溯支持，推动可信系统发展。

## 📝 摘要（中文）

图表因其高信息密度和直观可读性，已成为跨学科数据分析和交流的实际媒介。近年来，多模态大语言模型（MLLMs）在自动化图表理解方面取得了显著进展，但它们仍然严重依赖显式文本标注，并且在关键数字缺失时性能显著下降。为解决这一局限性，我们引入了ChartAgent，这是一个基于工具集成推理（TIR）的图表理解框架。受人类认知启发，ChartAgent将复杂的图表分析分解为一系列可观察、可重放的步骤。支持这一架构的是一个可扩展的模块化工具库，包含十多个核心工具，如关键元素检测、实例分割和光学字符识别（OCR），智能体动态编排这些工具，以实现跨不同图表类型的系统化视觉解析。利用TIR的透明性和可验证性，ChartAgent超越了黑盒范式，通过将中间输出标准化并整合为结构化证据包，为最终结论提供可追溯和可复现的支持。实验表明，ChartAgent在稀疏标注设置下显著提高了鲁棒性，为可信赖和可扩展的图表理解系统提供了一条实用路径。

## 🔬 方法详解

ChartAgent是一个基于工具集成推理（TIR）的图表理解框架。整体框架将复杂图表分析分解为可观察、可重放的步骤序列，通过一个可扩展的模块化工具库（包括关键元素检测、实例分割、OCR等十多个核心工具）动态编排实现系统化视觉解析。关键技术创新点在于引入结构化证据包，标准化和整合中间输出，提供可追溯和可复现的支持。与现有方法的主要区别在于，它超越了MLLMs的黑盒范式，通过工具集成提高鲁棒性，特别是在稀疏标注或关键信息缺失场景下，增强了透明性和可信度。

## 📊 实验亮点

实验结果表明，ChartAgent在稀疏标注设置下显著提升了鲁棒性，通过工具集成推理和结构化证据包，实现了可追溯的图表解析，为可信赖的自动化系统提供了有效解决方案。

## 🎯 应用场景

该研究可应用于数据可视化分析、自动化报告生成、教育辅助工具和商业智能系统等领域，通过提高图表理解的鲁棒性和可解释性，支持跨学科的数据驱动决策和高效信息提取，具有广泛的实用价值。

## 📄 摘要（原文）

> With their high information density and intuitive readability, charts have become the de facto medium for data analysis and communication across disciplines. Recent multimodal large language models (MLLMs) have made notable progress in automated chart understanding, yet they remain heavily dependent on explicit textual annotations and the performance degrades markedly when key numerals are absent. To address this limitation, we introduce ChartAgent, a chart understanding framework grounded in Tool-Integrated Reasoning (TIR). Inspired by human cognition, ChartAgent decomposes complex chart analysis into a sequence of observable, replayable steps. Supporting this architecture is an extensible, modular tool library comprising more than a dozen core tools, such as keyelement detection, instance segmentation, and optical character recognition (OCR), which the agent dynamically orchestrates to achieve systematic visual parsing across diverse chart types. Leveraging TIRs transparency and verifiability, ChartAgent moves beyond the black box paradigm by standardizing and consolidating intermediate outputs into a structured Evidence Package, providing traceable and reproducible support for final conclusions. Experiments show that ChartAgent substantially improves robustness under sparse annotation settings, offering a practical path toward trustworthy and extensible systems for chart understanding.

