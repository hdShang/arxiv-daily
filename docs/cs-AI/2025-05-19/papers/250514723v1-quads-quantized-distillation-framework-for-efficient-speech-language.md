---
layout: default
title: QUADS: QUAntized Distillation Framework for Efficient Speech Language Understanding
---

# QUADS: QUAntized Distillation Framework for Efficient Speech Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14723" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14723v1</a>
  <a href="https://arxiv.org/pdf/2505.14723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14723v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14723v1', 'QUADS: QUAntized Distillation Framework for Efficient Speech Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Subrata Biswas, Mohammad Nur Hossain Khan, Bashima Islam

**分类**: eess.AS, cs.AI, cs.CL, cs.LG, cs.SD

**发布日期**: 2025-05-19

**期刊**: INTERSPEECH, 2025

**DOI**: [10.21437/Interspeech.2025-532](https://doi.org/10.21437/Interspeech.2025-532)

---

## 💡 一句话要点

**提出QUADS框架以解决资源受限环境下的语音语言理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `语音语言理解` `蒸馏训练` `量化优化` `模型压缩` `资源受限环境`

## 📋 核心要点

1. 现有的蒸馏和量化方法分别处理，导致在压缩性能上存在不足，无法有效结合两者的优势。
2. QUADS框架通过多阶段训练和预调模型的结合，统一优化蒸馏和量化，提升了模型在低比特率下的适应性。
3. QUADS在SLURP和FSC数据集上分别取得了71.13%和99.20%的准确率，且计算复杂度和模型大小显著降低，表现出色。

## 📝 摘要（中文）

语音语言理解（SLU）系统必须在性能和效率之间取得平衡，尤其是在资源受限的环境中。现有方法分别应用蒸馏和量化，导致压缩效果不佳，因为蒸馏忽略了量化约束。我们提出了QUADS，一个统一框架，通过多阶段训练与预调模型相结合，优化了蒸馏和量化的过程，增强了对低比特率的适应性，同时保持了准确性。QUADS在SLURP数据集上达到了71.13%的准确率，在FSC数据集上达到了99.20%的准确率，与最先进模型相比，仅有最多5.56%的轻微下降。此外，它将计算复杂度降低了60至73倍（GMACs），模型大小减少了83至700倍，展示了在极端量化下的强大鲁棒性。这些结果确立了QUADS作为现实世界资源受限SLU应用的高效解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有语音语言理解（SLU）系统在资源受限环境下的性能与效率平衡问题。现有方法在蒸馏和量化过程中未能有效结合，导致压缩效果不理想。

**核心思路**：QUADS框架的核心思想是通过多阶段训练与预调模型的结合，统一优化蒸馏和量化过程，从而在保持准确性的同时增强模型对低比特率的适应性。

**技术框架**：QUADS的整体架构包括多个训练阶段，首先使用预调模型进行初步训练，然后在此基础上进行蒸馏和量化的联合优化。主要模块包括模型预调、蒸馏训练和量化优化。

**关键创新**：QUADS的主要创新在于将蒸馏与量化过程整合为一个统一的框架，解决了传统方法中蒸馏与量化相互独立的问题，从而显著提升了模型的压缩效率和性能。

**关键设计**：在QUADS中，关键设计包括选择合适的损失函数以平衡蒸馏和量化目标，以及在网络结构中引入适应低比特率的模块，确保模型在极端量化条件下仍能保持较高的准确性。

## 📊 实验亮点

QUADS在SLURP数据集上实现了71.13%的准确率，在FSC数据集上达到了99.20%的准确率，且与最先进模型相比，准确率仅下降最多5.56%。此外，QUADS显著降低了计算复杂度60至73倍，模型大小减少83至700倍，展示了在极端量化下的强大鲁棒性。

## 🎯 应用场景

QUADS框架在资源受限的语音语言理解应用中具有广泛的潜在应用价值，如智能助手、语音识别设备和移动端应用等。通过提高模型的压缩效率和性能，QUADS能够在实际应用中实现更快的响应速度和更低的资源消耗，推动SLU技术的普及与发展。

## 📄 摘要（原文）

> Spoken Language Understanding (SLU) systems must balance performance and efficiency, particularly in resource-constrained environments. Existing methods apply distillation and quantization separately, leading to suboptimal compression as distillation ignores quantization constraints. We propose QUADS, a unified framework that optimizes both through multi-stage training with a pre-tuned model, enhancing adaptability to low-bit regimes while maintaining accuracy. QUADS achieves 71.13\% accuracy on SLURP and 99.20\% on FSC, with only minor degradations of up to 5.56\% compared to state-of-the-art models. Additionally, it reduces computational complexity by 60--73$\times$ (GMACs) and model size by 83--700$\times$, demonstrating strong robustness under extreme quantization. These results establish QUADS as a highly efficient solution for real-world, resource-constrained SLU applications.

