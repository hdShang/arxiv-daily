---
layout: default
title: "AccidentBench: Benchmarking Multimodal Understanding and Reasoning in Vehicle Accidents and Beyond"
---

# AccidentBench: Benchmarking Multimodal Understanding and Reasoning in Vehicle Accidents and Beyond

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26636" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26636v1</a>
  <a href="https://arxiv.org/pdf/2509.26636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26636v1', 'AccidentBench: Benchmarking Multimodal Understanding and Reasoning in Vehicle Accidents and Beyond')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangding Gu, Xiaohan Wang, Donghao Ying, Haoyu Zhao, Runing Yang, Ming Jin, Boyi Li, Marco Pavone, Serena Yeung-Levy, Jun Wang, Dawn Song, Costas Spanos

**分类**: cs.LG

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/SafeRL-Lab/AccidentBench)

---

## 💡 一句话要点

**AccidentBench：构建大规模多模态基准，评估车辆事故及其他安全场景下的理解与推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `安全关键场景` `事故分析` `时空推理` `意图理解` `基准数据集` `自动驾驶` `视频问答`

## 📋 核心要点

1. 现有方法在安全关键的动态真实世界场景中，对多模态信息的理解和推理能力不足，尤其是在时间和空间推理方面。
2. AccidentBench通过构建包含车辆事故和航空、水运等场景的大规模数据集，系统性地评估模型在时间、空间和意图理解与推理方面的能力。
3. 实验表明，即使是最先进的模型在AccidentBench中最困难的任务上表现仍然很差，突显了现有模型在真实世界推理方面的差距。

## 📝 摘要（中文）

本文提出了AccidentBench，一个大规模基准数据集，旨在严格评估多模态模型在安全关键、动态真实世界环境中的理解和推理能力。该基准结合了车辆事故场景以及航空和水运等“超越”领域，这些领域强调空间和时间推理（例如，导航、方向、多车辆运动）。AccidentBench包含约2000个视频和超过19000个人工标注的问答对，涵盖多种视频长度（短/中/长）和难度级别（易/中/难）。任务系统性地探究了时间、空间和意图理解与推理的核心能力。通过将以事故为中心的交通场景与更广泛的航空和水运安全关键场景相结合，AccidentBench提供了一个全面的、物理基础的测试平台，用于评估模型在真实世界可变性下的表现。对最先进模型（例如，Gemini-2.5 Pro和GPT-5）的评估表明，即使是最强大的模型在最困难的任务和最长的视频上，准确率也仅达到约18%，揭示了真实世界时间、空间和意图推理方面的巨大差距。AccidentBench旨在暴露这些关键差距，并推动多模态模型的发展，使其更安全、更稳健，并更好地应对真实世界的安全关键挑战。代码和数据集可在https://github.com/SafeRL-Lab/AccidentBench获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态模型在安全关键场景下，特别是涉及复杂时空推理和意图理解的任务中表现不佳的问题。现有方法难以有效处理真实世界场景中的可变性和复杂性，导致在事故预测和安全决策等任务中存在较大风险。

**核心思路**：论文的核心思路是构建一个大规模、多样化的基准数据集，涵盖车辆事故以及航空、水运等安全关键场景，并设计一系列具有挑战性的问答任务，以系统性地评估模型在时间、空间和意图理解与推理方面的能力。通过暴露现有模型的弱点，推动更安全、更鲁棒的多模态模型的发展。

**技术框架**：AccidentBench数据集包含约2000个视频和超过19000个人工标注的问答对。数据集涵盖多种视频长度（短/中/长）和难度级别（易/中/难）。任务设计围绕时间推理（例如，事件顺序、持续时间）、空间推理（例如，物体位置、相对关系）和意图理解（例如，驾驶员意图、潜在风险）展开。数据集的构建过程注重场景的多样性和真实性，以模拟真实世界中的复杂情况。

**关键创新**：AccidentBench的关键创新在于其综合性地结合了车辆事故场景与航空、水运等“超越”领域，从而提供了一个更全面、更具挑战性的测试平台。此外，该基准系统性地探究了时间、空间和意图理解与推理的核心能力，为多模态模型的发展提供了明确的方向。

**关键设计**：数据集中的问答对由人工标注，确保了标注的准确性和一致性。任务难度分级通过控制问题的复杂性和所需推理的深度来实现。视频长度的变化旨在评估模型对长期依赖关系的建模能力。此外，数据集还包含了多种类型的事故和安全事件，以增加场景的多样性。

## 📊 实验亮点

实验结果表明，即使是像Gemini-2.5 Pro和GPT-5这样最先进的模型，在AccidentBench中最困难的任务和最长的视频上，准确率也仅达到约18%。这突显了现有模型在真实世界时间、空间和意图推理方面存在显著差距，表明AccidentBench能够有效暴露现有模型的弱点。

## 🎯 应用场景

AccidentBench的研究成果可应用于自动驾驶、智能交通、航空安全、水运安全等领域。通过提升多模态模型在安全关键场景下的理解和推理能力，可以有效降低事故发生率，提高安全保障水平，并为智能决策提供更可靠的支持。

## 📄 摘要（原文）

> Rapid advances in multimodal models demand benchmarks that rigorously evaluate understanding and reasoning in safety-critical, dynamic real-world settings. We present AccidentBench, a large-scale benchmark that combines vehicle accident scenarios with Beyond domains, safety-critical settings in air and water that emphasize spatial and temporal reasoning (e.g., navigation, orientation, multi-vehicle motion). The benchmark contains approximately 2000 videos and over 19000 human-annotated question--answer pairs spanning multiple video lengths (short/medium/long) and difficulty levels (easy/medium/hard). Tasks systematically probe core capabilities: temporal, spatial, and intent understanding and reasoning. By unifying accident-centric traffic scenes with broader safety-critical scenarios in air and water, AccidentBench offers a comprehensive, physically grounded testbed for evaluating models under real-world variability. Evaluations of state-of-the-art models (e.g., Gemini-2.5 Pro and GPT-5) show that even the strongest models achieve only about 18% accuracy on the hardest tasks and longest videos, revealing substantial gaps in real-world temporal, spatial, and intent reasoning. AccidentBench is designed to expose these critical gaps and drive the development of multimodal models that are safer, more robust, and better aligned with real-world safety-critical challenges. The code and dataset are available at: https://github.com/SafeRL-Lab/AccidentBench

