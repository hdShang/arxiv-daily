---
layout: default
title: Leveraging LLMs to Automate Energy-Aware Refactoring of Parallel Scientific Codes
---

# Leveraging LLMs to Automate Energy-Aware Refactoring of Parallel Scientific Codes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02184" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02184v2</a>
  <a href="https://arxiv.org/pdf/2505.02184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02184v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02184v2', 'Leveraging LLMs to Automate Energy-Aware Refactoring of Parallel Scientific Codes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthew T. Dearing, Yiheng Tao, Xingfu Wu, Zhiling Lan, Valerie Taylor

**分类**: cs.AI, cs.DC, cs.PL, cs.SE

**发布日期**: 2025-05-04 (更新: 2025-11-05)

**备注**: 12 pages, 4 figures, version under review at a peer-reviewed conference

---

## 💡 一句话要点

**提出LASSI-EE框架以自动化能源感知并行科学代码重构**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `能效优化` `并行计算` `自动化重构` `科学代码生成` `多阶段迭代` `性能评估`

## 📋 核心要点

1. 现有方法在生成并行科学代码时，往往忽视了能效，导致性能不足。
2. LASSI-EE框架通过多阶段迭代方法，结合能效感知提示和自我纠正机制，自动生成高能效代码。
3. 实验结果显示，LASSI-EE在多次尝试下可实现平均48%的能量减少，且在不同硬件上表现一致。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在生成并行科学代码中的应用日益增多，现有研究往往侧重于功能正确性，而忽视了性能，尤其是能效。本文提出了LASSI-EE，一个基于LLM的自动化重构框架，通过多阶段迭代方法生成能效高的并行代码，集成了运行时功率分析、能效感知提示、自我纠正反馈循环及LLM作为评判者的自动筛选机制。我们引入了energy-reduction@k这一新颖指标，量化生成k个代码候选时的预期能量减少，便于系统评估多次尝试生成策略。对20个HeCBench应用和两个miniApps在NVIDIA A100和AMD MI100 GPU上的评估显示，单次运行（k=1）下，LASSI-EE生成的重构并行代码平均预期能量减少29%，通过率为81%，相比于传统LLM提示提升了2.8倍。多次运行（k=3）则实现了平均48%的预期能量减少和97%的通过率。这些结果在不同硬件架构上均表现出一致性，证明了LASSI-EE的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有并行科学代码生成方法在能效方面的不足，尤其是缺乏对性能优化的关注。

**核心思路**：LASSI-EE框架通过集成多种技术手段，如运行时功率分析和自我纠正反馈，来生成能效更高的并行代码，确保在功能正确的基础上提升能效。

**技术框架**：LASSI-EE的整体架构包括多个模块：首先进行运行时功率分析，接着通过能效感知提示生成代码，再利用自我纠正反馈循环优化代码，最后由LLM作为评判者进行自动筛选。

**关键创新**：引入energy-reduction@k指标，量化生成k个代码候选时的预期能量减少，提供了一种系统评估多次尝试生成策略的新方法。

**关键设计**：在参数设置上，LASSI-EE采用了多次尝试生成策略，k值的选择直接影响能效的提升，实验中k=1和k=3的对比显示了显著的性能差异。损失函数和网络结构的设计也针对能效优化进行了特别调整。

## 📊 实验亮点

实验结果表明，LASSI-EE在单次运行（k=1）下实现了平均29%的能量减少，且通过率达到81%；在多次运行（k=3）时，能量减少率提升至48%，通过率达到97%。这些结果在不同硬件架构上均表现出一致性，显示出该框架的广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括高性能计算、科学模拟和大规模数据处理等，能够为科学研究提供更为高效的代码生成工具，降低能耗，提升计算资源的利用率。未来，LASSI-EE框架有望在更广泛的并行计算任务中得到应用，推动可持续计算的发展。

## 📄 摘要（原文）

> While large language models (LLMs) are increasingly used for generating parallel scientific codes, most efforts emphasize functional correctness, often overlooking performance, especially energy efficiency. We propose LASSI-EE, an automated LLM-based refactoring framework that generates energy-efficient parallel codes through a multi-stage, iterative approach integrating runtime power profiling, energy-aware prompting, self-correcting feedback loops, and an LLM-as-a-Judge agent for automated screening of code solutions. We introduce energy-reduction@k, a novel metric that quantifies expected energy reduction when generating k code candidates and selecting the most energy-efficient, enabling systematic evaluation of multi-attempt generation strategies. Evaluating 20 HeCBench applications and two miniApps on NVIDIA A100 and AMD MI100 GPUs, a single run (k=1) with LASSI-EE delivers refactored parallel codes with an average 29% expected energy reduction at an 81% pass rate, representing a 2.8x improvement over vanilla LLM prompting. Multiple runs (k=3) achieve an average 48% expected energy reduction at a 97% pass rate. These results are consistent across devices, demonstrating LASSI-EE's effectiveness across diverse hardware architectures.

