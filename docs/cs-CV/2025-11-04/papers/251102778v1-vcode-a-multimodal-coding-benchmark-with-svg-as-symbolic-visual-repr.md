---
layout: default
title: VCode: a Multimodal Coding Benchmark with SVG as Symbolic Visual Representation
---

# VCode: a Multimodal Coding Benchmark with SVG as Symbolic Visual Representation

**arXiv**: [2511.02778v1](https://arxiv.org/abs/2511.02778) | [PDF](https://arxiv.org/pdf/2511.02778.pdf)

**作者**: Kevin Qinghong Lin, Yuhao Zheng, Hangyu Ran, Dantong Zhu, Dongxing Mao, Linjie Li, Philip Torr, Alex Jinpeng Wang

---

## 💡 一句话要点

**提出VCode基准与VCoder框架，以SVG作为符号视觉表示解决多模态理解问题**

**关键词**: `多模态编码基准` `SVG符号表示` `代码生成评估` `视觉语言模型增强` `迭代修订框架` `视觉工具集成`

## 📋 核心要点

1. 核心问题：视觉中心编码在代理时代被忽视，现有模型难以生成忠实符号视觉表示
2. 方法要点：引入SVG代码作为紧凑可执行表示，并开发VCoder框架通过迭代修订和视觉工具增强VLM
3. 实验或效果：VCoder在基准上优于Claude-4-Opus 12.3分，人类与VLM在SVG上表现一致

## 📄 摘要（原文）

> Code has emerged as a precise and executable medium for reasoning and action
> in the agent era. Yet, progress has largely focused on language-centric tasks
> such as program synthesis and debugging, leaving visual-centric coding
> underexplored. Inspired by how humans reason over sketches, we advocate SVG
> code as a compact, interpretable, and executable visual representation. We
> introduce VCode, a benchmark that reframes multimodal understanding as code
> generation: given an image, a model must produce SVG that preserves symbolic
> meaning for downstream reasoning. VCode covers three domains - general
> commonsense (MM-Vet), professional disciplines (MMMU), and visual-centric
> perception (CV-Bench). To assess symbolic fidelity, we propose CodeVQA, a novel
> evaluation protocol in which a policy model answers questions over rendered
> SVGs; correct answers indicate faithful symbolic preservation. Empirically,
> frontier VLMs struggle to generate faithful SVGs, revealing a persistent gap
> between language-centric and visual-centric coding. To close this gap, we
> introduce VCoder, an agentic framework that augments VLMs along two axes: (i)
> Thinking with Revision, which iteratively analyzes discrepancies and refines
> SVG code; and (ii) Acting with Visual Tools, where detectors and parsers supply
> structured cues such as objects, shapes, and text beyond the model's intrinsic
> capacity. Across benchmarks, frontier VLMs with strong reasoning capabilities
> score well overall yet remain limited in professional knowledge and 3D
> reasoning. VCoder delivers a 12.3-point overall gain over the top-performing
> Claude-4-Opus. Human studies show that both humans and VLMs perform worse on
> rendered SVGs, their consistency reveals the promise of symbolic visual
> representation. The benchmark and code are available at
> https://github.com/CSU-JPG/VCode.

