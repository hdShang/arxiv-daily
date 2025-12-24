---
layout: default
title: Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking
---

# Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20199" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20199v1</a>
  <a href="https://arxiv.org/pdf/2505.20199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20199v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20199v1', 'Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengxiang Li, Shilin Yan, Joey Tsai, Renrui Zhang, Ruichuan An, Ziyu Guo, Xiaowei Gao

**分类**: cs.CL

**发布日期**: 2025-05-26

**备注**: Project page: https://github.com/pixeli99/A-CFG

---

## 💡 一句话要点

**提出自适应无分类器引导以解决生成模型中的不确定性问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `自适应引导` `生成模型` `无分类器引导` `动态掩蔽` `语言生成`

## 📋 核心要点

1. 现有的无分类器引导方法在处理动态不确定性时，通常依赖静态的无条件输入，导致生成效果不佳。
2. 本文提出的自适应无分类器引导（A-CFG）通过动态调整无条件输入，专注于模型信心低的标记，从而提高生成质量。
3. 实验结果显示，A-CFG在多项语言生成任务中表现优异，相较于标准CFG，GPQA任务上提升了3.9分。

## 📝 摘要（中文）

无分类器引导（CFG）通过插值条件和无条件预测显著增强了生成模型的可控性。然而，标准CFG通常使用静态的无条件输入，这在模型不确定性动态变化的迭代生成过程中可能表现不佳。本文提出自适应无分类器引导（A-CFG），通过利用模型的瞬时预测信心来调整无条件输入。在每一步的迭代（掩蔽）扩散语言模型中，A-CFG识别当前生成序列中模型信心低的标记，并暂时重新掩蔽这些标记，以创建动态的局部无条件输入。这种方法使CFG的纠正影响精准集中在模糊区域，从而实现更有效的引导。我们将A-CFG集成到最先进的掩蔽扩散语言模型中，并展示其有效性。实验结果表明，A-CFG在多种语言生成基准上显著优于标准CFG，例如在GPQA上提升了3.9分。

## 🔬 方法详解

**问题定义**：本文旨在解决生成模型中由于静态无条件输入导致的低效引导问题，特别是在模型不确定性动态变化的情况下，现有方法无法有效应对。

**核心思路**：A-CFG的核心思想是根据模型的即时预测信心动态调整无条件输入，通过重新掩蔽低信心的标记，集中引导模型在模糊区域的生成。

**技术框架**：A-CFG的整体架构包括两个主要模块：首先是信心评估模块，用于识别低信心标记；其次是动态掩蔽模块，根据识别结果调整无条件输入，形成局部引导。

**关键创新**：A-CFG的创新在于其动态适应性，通过实时评估模型信心来调整引导策略，这与传统的静态CFG方法形成鲜明对比。

**关键设计**：在设计中，A-CFG采用了特定的阈值来判断低信心标记，并结合掩蔽机制进行动态调整，确保引导的有效性和针对性。具体的损失函数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，A-CFG在多种语言生成基准上显著优于标准CFG，尤其是在GPQA任务上实现了3.9分的提升，显示出其在动态引导机制上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言生成、对话系统和文本补全等。通过提高生成模型在不确定性情况下的表现，A-CFG能够为实际应用提供更高质量的生成结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions. However, standard CFG often employs a static unconditional input, which can be suboptimal for iterative generation processes where model uncertainty varies dynamically. We introduce Adaptive Classifier-Free Guidance (A-CFG), a novel method that tailors the unconditional input by leveraging the model's instantaneous predictive confidence. At each step of an iterative (masked) diffusion language model, A-CFG identifies tokens in the currently generated sequence for which the model exhibits low confidence. These tokens are temporarily re-masked to create a dynamic, localized unconditional input. This focuses CFG's corrective influence precisely on areas of ambiguity, leading to more effective guidance. We integrate A-CFG into a state-of-the-art masked diffusion language model and demonstrate its efficacy. Experiments on diverse language generation benchmarks show that A-CFG yields substantial improvements over standard CFG, achieving, for instance, a 3.9 point gain on GPQA. Our work highlights the benefit of dynamically adapting guidance mechanisms to model uncertainty in iterative generation.

