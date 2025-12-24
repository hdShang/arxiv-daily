---
layout: default
title: "DiagnosisArena: Benchmarking Diagnostic Reasoning for Large Language Models"
---

# DiagnosisArena: Benchmarking Diagnostic Reasoning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14107" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14107v4</a>
  <a href="https://arxiv.org/pdf/2505.14107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14107v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14107v4', 'DiagnosisArena: Benchmarking Diagnostic Reasoning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yakun Zhu, Zhongzhen Huang, Linjie Mu, Yutong Huang, Wei Nie, Jiaji Liu, Shaoting Zhang, Pengfei Liu, Xiaofan Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-29)

**🔗 代码/项目**: [GITHUB](https://github.com/SPIRAL-MED/DiagnosisArena)

---

## 💡 一句话要点

**提出DiagnosisArena以评估大型语言模型的诊断推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `诊断推理` `医学基准` `AI应用` `临床案例`

## 📋 核心要点

1. 现有医学基准在评估大型语言模型的高级诊断推理能力方面存在显著不足，无法有效支持临床应用。
2. DiagnosisArena是一个新提出的基准，旨在通过1,113对患者案例和诊断的系统评估，提升模型的诊断推理能力。
3. 实验结果显示，当前最先进的模型在DiagnosisArena上的表现不佳，准确率分别为51.12%、31.09%和17.79%，揭示了模型的泛化瓶颈。

## 📝 摘要（中文）

大型语言模型在复杂推理任务中的崛起为解决科学挑战带来了希望，尤其是在复杂的临床场景中。为了确保这些模型在现实医疗环境中的安全有效部署，迫切需要系统地基准测试当前模型的诊断能力。现有医学基准在评估高级诊断推理方面存在局限，因此我们提出了DiagnosisArena，这是一个全面且具有挑战性的基准，旨在严格评估专业级诊断能力。DiagnosisArena包含1,113对分段患者案例及相应诊断，涵盖28个医学专业，来源于10本顶级医学期刊的临床案例报告。基准的开发经过多轮筛选和审查，由AI系统和人类专家共同完成，确保数据不泄露。我们的研究表明，即使是最先进的推理模型，其准确率也仅为51.12%、31.09%和17.79%，这突显了当前大型语言模型在临床诊断推理挑战中的显著泛化瓶颈。

## 🔬 方法详解

**问题定义**：论文旨在解决当前大型语言模型在临床诊断推理中的评估不足，现有方法无法有效反映模型的真实能力和泛化性能。

**核心思路**：通过构建DiagnosisArena基准，系统性地评估模型的专业级诊断能力，确保评估的全面性和挑战性，以推动AI在医疗领域的应用。

**技术框架**：DiagnosisArena的开发包括多个阶段，首先是从顶级医学期刊中筛选临床案例，然后进行分段和标注，最后通过AI和专家的多轮审查确保数据质量。

**关键创新**：DiagnosisArena的创新在于其系统性和挑战性，涵盖28个医学专业的1,113对案例，能够更全面地评估模型的诊断推理能力，与现有基准相比具有更高的专业性和实用性。

**关键设计**：在基准构建过程中，采用了严格的筛选标准和审查流程，确保数据的准确性和可靠性，同时设计了多种评估指标，以全面反映模型的性能。

## 📊 实验亮点

在DiagnosisArena基准测试中，最先进的推理模型o3、o1和DeepSeek-R1的准确率分别为51.12%、31.09%和17.79%。这些结果表明，当前模型在临床诊断推理方面存在显著的泛化瓶颈，亟需进一步研究和改进。

## 🎯 应用场景

DiagnosisArena的研究成果具有广泛的应用潜力，特别是在医疗人工智能领域。通过提供一个系统的评估工具，研究人员和开发者可以更好地理解和提升大型语言模型在临床诊断中的应用能力，从而推动智能医疗的发展，改善患者的诊断和治疗效果。

## 📄 摘要（原文）

> The emergence of groundbreaking large language models capable of performing complex reasoning tasks holds significant promise for addressing various scientific challenges, including those arising in complex clinical scenarios. To enable their safe and effective deployment in real-world healthcare settings, it is urgently necessary to benchmark the diagnostic capabilities of current models systematically. Given the limitations of existing medical benchmarks in evaluating advanced diagnostic reasoning, we present DiagnosisArena, a comprehensive and challenging benchmark designed to rigorously assess professional-level diagnostic competence. DiagnosisArena consists of 1,113 pairs of segmented patient cases and corresponding diagnoses, spanning 28 medical specialties, deriving from clinical case reports published in 10 top-tier medical journals. The benchmark is developed through a meticulous construction pipeline, involving multiple rounds of screening and review by both AI systems and human experts, with thorough checks conducted to prevent data leakage. Our study reveals that even the most advanced reasoning models, o3, o1, and DeepSeek-R1, achieve only 51.12%, 31.09%, and 17.79% accuracy, respectively. This finding highlights a significant generalization bottleneck in current large language models when faced with clinical diagnostic reasoning challenges. Through DiagnosisArena, we aim to drive further advancements in AI's diagnostic reasoning capabilities, enabling more effective solutions for real-world clinical diagnostic challenges. We provide the benchmark and evaluation tools for further research and development https://github.com/SPIRAL-MED/DiagnosisArena.

