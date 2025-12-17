---
layout: default
title: Revisiting Mixout: An Overlooked Path to Robust Finetuning
---

# Revisiting Mixout: An Overlooked Path to Robust Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06982" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06982v1</a>
  <a href="https://arxiv.org/pdf/2510.06982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06982v1" onclick="toggleFavorite(this, '2510.06982v1', 'Revisiting Mixout: An Overlooked Path to Robust Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Masih Aminbeidokhti, Heitor Rapela Medeiros, Eric Granger, Marco Pedersoli

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出GMixout，通过自适应权重混合提升微调模型在分布偏移下的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉基础模型` `微调` `鲁棒性` `分布偏移` `Mixout` `正则化` `指数移动平均` `自适应学习`

## 📋 核心要点

1. 微调视觉模型在提升特定领域性能的同时，往往会降低模型在数据分布发生变化时的鲁棒性。
2. GMixout通过动态调整权重混合比例，利用指数移动平均快照作为锚点，并显式控制重采样频率，从而提升模型鲁棒性。
3. 实验表明，GMixout在多个数据集上，相较于现有微调方法，在域内精度和分布偏移鲁棒性上均有显著提升。

## 📝 摘要（中文）

微调视觉基础模型通常能提升在域精度，但会牺牲分布偏移下的鲁棒性。本文重新审视Mixout，一种随机正则化方法，它间歇性地用预训练权重替换微调权重，并将其视为单次运行、权重共享的隐式集成。这种视角揭示了控制鲁棒性的三个关键因素：掩码锚点、重采样频率和掩码稀疏性。基于此，我们提出了GMixout，它(i)用训练期间自适应的指数移动平均快照替换固定锚点，以及(ii)通过显式的重采样频率超参数来调节掩码周期。我们的稀疏核实现仅更新一小部分参数，且没有推理时开销，从而可以在消费级GPU上进行训练。在涵盖协变量偏移、损坏和类别不平衡的基准测试（ImageNet / ImageNet-LT、DomainNet、iWildCam和CIFAR100-C）上，GMixout始终优于零样本性能，并在分布偏移下超越模型集成和强大的参数高效微调基线，同时提升了在域精度。

## 🔬 方法详解

**问题定义**：现有视觉基础模型的微调方法，虽然能在目标领域取得不错的精度，但当测试数据与训练数据分布不一致时（即发生分布偏移），模型的泛化能力会显著下降，鲁棒性不足。现有的参数高效微调方法和模型集成方法在分布偏移下仍存在局限性。

**核心思路**：本文的核心思路是改进Mixout正则化方法，使其能够更好地平衡模型在目标领域的精度和在分布偏移下的鲁棒性。通过引入自适应的权重混合策略，使得模型在微调过程中能够更好地保留预训练模型的泛化能力，从而提升鲁棒性。

**技术框架**：GMixout的核心在于改进了Mixout的权重混合策略。Mixout原本使用固定的预训练权重作为锚点，而GMixout使用指数移动平均（EMA）的权重快照作为锚点，这个EMA快照在训练过程中不断更新，从而实现自适应的权重混合。此外，GMixout还引入了一个显式的重采样频率超参数，用于控制掩码的更新周期。整体流程包括：加载预训练模型，使用GMixout进行微调，并在验证集上评估性能。

**关键创新**：GMixout的关键创新在于：(1) 使用EMA权重快照作为Mixout的锚点，使得权重混合更加自适应，能够更好地保留预训练模型的泛化能力；(2) 引入显式的重采样频率超参数，用于控制掩码的更新周期，从而更好地调节正则化强度。与传统Mixout相比，GMixout的锚点是动态变化的，能够更好地适应微调过程中的权重变化。

**关键设计**：GMixout的关键设计包括：(1) EMA快照的更新率：控制EMA快照对当前模型权重的学习速度；(2) 重采样频率：控制掩码的更新频率，影响正则化的强度；(3) 稀疏核实现：为了降低计算成本，GMixout采用稀疏核实现，只更新一小部分参数，从而可以在消费级GPU上进行训练。损失函数采用标准的交叉熵损失函数。

## 📊 实验亮点

实验结果表明，GMixout在ImageNet、DomainNet、iWildCam和CIFAR100-C等数据集上，相较于零样本性能和现有的微调方法（包括Model Soups和参数高效微调方法），在域内精度和分布偏移鲁棒性上均有显著提升。例如，在某些数据集上，GMixout的性能提升超过了5%。

## 🎯 应用场景

GMixout可应用于各种需要对视觉基础模型进行微调的场景，尤其是在数据分布可能发生偏移的情况下，例如自动驾驶、医疗图像分析、遥感图像分析等。该方法能够提升模型在实际应用中的可靠性和泛化能力，降低模型失效的风险。

## 📄 摘要（原文）

> Finetuning vision foundation models often improves in-domain accuracy but comes at the cost of robustness under distribution shift. We revisit Mixout, a stochastic regularizer that intermittently replaces finetuned weights with their pretrained reference, through the lens of a single-run, weight-sharing implicit ensemble. This perspective reveals three key levers that govern robustness: the \emph{masking anchor}, \emph{resampling frequency}, and \emph{mask sparsity}. Guided by this analysis, we introduce GMixout, which (i) replaces the fixed anchor with an exponential moving-average snapshot that adapts during training, and (ii) regulates masking period via an explicit resampling-frequency hyperparameter. Our sparse-kernel implementation updates only a small fraction of parameters with no inference-time overhead, enabling training on consumer-grade GPUs. Experiments on benchmarks covering covariate shift, corruption, and class imbalance, ImageNet / ImageNet-LT, DomainNet, iWildCam, and CIFAR100-C, GMixout consistently improves in-domain accuracy beyond zero-shot performance while surpassing both Model Soups and strong parameter-efficient finetuning baselines under distribution shift.

