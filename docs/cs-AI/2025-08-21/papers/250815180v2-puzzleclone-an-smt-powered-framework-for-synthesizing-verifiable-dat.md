---
layout: default
title: "PuzzleClone: An SMT-Powered Framework for Synthesizing Verifiable Data"
---

# PuzzleClone: An SMT-Powered Framework for Synthesizing Verifiable Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15180" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15180v2</a>
  <a href="https://arxiv.org/pdf/2508.15180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15180v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15180v2', 'PuzzleClone: An SMT-Powered Framework for Synthesizing Verifiable Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Xiong, Yanwei Huang, Rongjunchen Zhang, Kun Chen, Haipang Wu

**分类**: cs.AI

**发布日期**: 2025-08-21 (更新: 2025-08-25)

**🔗 代码/项目**: [GITHUB](https://github.com/HiThink-Research/PuzzleClone)

---

## 💡 一句话要点

**提出PuzzleClone框架以合成可验证数据解决LLM训练问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据合成` `可验证数据` `逻辑推理` `数学问题` `大型语言模型` `SMT技术` `模型训练`

## 📋 核心要点

1. 现有的LLM生成数据集在可靠性、丰富性和可扩展性方面存在不足，限制了模型的推理能力。
2. PuzzleClone框架通过将种子难题编码为逻辑规范、随机化生成变体以及重现机制确保有效性，提供了系统化的解决方案。
3. 在PuzzleClone数据集上进行后续训练后，模型在多个逻辑和数学基准上表现出显著提升，平均分数从14.4提高到56.2。

## 📝 摘要（中文）

高质量的数学和逻辑数据集对于增强大型语言模型（LLMs）的推理能力至关重要。尽管近期的数据增强技术促进了大规模基准的创建，但现有的LLM生成数据集往往存在可靠性、丰富性和可扩展性不足的问题。为了解决这些挑战，本文提出了PuzzleClone，一个基于可满足性理论（SMT）的正式框架，用于大规模合成可验证数据。该方法包括三个关键创新：将种子难题编码为结构化逻辑规范，通过系统的变量和约束随机化生成可扩展的变体，以及通过重现机制确保有效性。应用PuzzleClone，我们构建了一个包含超过83K个多样化且经过程序验证的难题的基准，生成的难题涵盖了广泛的难度和格式，对当前最先进的模型提出了显著挑战。实验结果表明，在PuzzleClone数据集上进行后续训练显著提高了模型性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM生成数据集在可靠性和多样性方面的不足，导致模型推理能力受限的问题。

**核心思路**：PuzzleClone框架通过系统化的逻辑规范编码和随机化生成数据，确保生成数据的有效性和多样性，从而提升模型的训练质量。

**技术框架**：该框架主要包括三个模块：1) 种子难题的逻辑规范编码；2) 通过变量和约束的随机化生成多样化的难题；3) 重现机制用于验证生成数据的有效性。

**关键创新**：PuzzleClone的创新在于其使用SMT技术系统化地生成可验证数据，与传统方法相比，显著提高了数据的可靠性和多样性。

**关键设计**：在生成过程中，采用了特定的参数设置和逻辑约束，确保生成的难题在难度和格式上具有广泛的覆盖，同时通过程序验证机制确保数据的有效性。

## 📊 实验亮点

实验结果显示，在PuzzleClone数据集上进行后续训练后，模型的平均分数从14.4提升至56.2，并在7个逻辑和数学基准上实现了最高12.5个百分点的绝对提升，表明该框架在提升模型性能方面的有效性。

## 🎯 应用场景

PuzzleClone框架的潜在应用领域包括教育、智能问答系统和自动化推理等。通过提供高质量的训练数据，能够显著提升大型语言模型在逻辑推理和数学问题上的表现，进而推动相关领域的研究和应用发展。

## 📄 摘要（原文）

> High-quality mathematical and logical datasets with verifiable answers are essential for strengthening the reasoning capabilities of large language models (LLMs). While recent data augmentation techniques have facilitated the creation of large-scale benchmarks, existing LLM-generated datasets often suffer from limited reliability, diversity, and scalability. To address these challenges, we introduce PuzzleClone, a formal framework for synthesizing verifiable data at scale using Satisfiability Modulo Theories (SMT). Our approach features three key innovations: (1) encoding seed puzzles into structured logical specifications, (2) generating scalable variants through systematic variable and constraint randomization, and (3) ensuring validity via a reproduction mechanism. Applying PuzzleClone, we construct a curated benchmark comprising over 83K diverse and programmatically validated puzzles. The generated puzzles span a wide spectrum of difficulty and formats, posing significant challenges to current state-of-the-art models. We conduct post training (SFT and RL) on PuzzleClone datasets. Experimental results show that training on PuzzleClone yields substantial improvements not only on PuzzleClone testset but also on logic and mathematical benchmarks. Post training raises PuzzleClone average from 14.4 to 56.2 and delivers consistent improvements across 7 logic and mathematical benchmarks up to 12.5 absolute percentage points (AMC2023 from 52.5 to 65.0). Our code and data are available at https://github.com/HiThink-Research/PuzzleClone.

