---
layout: default
title: Directional Reasoning Injection for Fine-Tuning MLLMs
---

# Directional Reasoning Injection for Fine-Tuning MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15050" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15050v1</a>
  <a href="https://arxiv.org/pdf/2510.15050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15050v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15050v1', 'Directional Reasoning Injection for Fine-Tuning MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Huang, Zeliang Zhang, Jiang Liu, Ximeng Sun, Jialian Wu, Xiaodong Yu, Ze Wang, Chenliang Xu, Emad Barsoum, Zicheng Liu

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: Project Page: https://wikichao.github.io/DRIFT/

---

## 💡 一句话要点

**提出DRIFT，通过梯度空间注入方向性推理知识，高效微调多模态大语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `推理能力` `梯度空间` `知识迁移` `模型微调`

## 📋 核心要点

1. 多模态大语言模型推理能力不足，现有微调方法成本高昂，模型合并效果不稳定。
2. DRIFT通过预计算推理先验，在梯度空间注入方向性推理知识，实现高效推理迁移。
3. 实验表明，DRIFT在推理基准上优于朴素合并和监督微调，且成本远低于训练密集型方法。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)发展迅速，但其推理能力通常落后于强大的纯文本模型。现有弥补差距的方法依赖于大规模多模态推理数据的监督微调或强化学习，两者都耗费资源。模型合并是一种有前景的替代方案，它在推理增强的LLM和多模态变体之间插值参数。然而，我们的分析表明，简单的合并并非总是“免费午餐”：其有效性在模型家族之间差异很大，一些模型（例如，LLaVA，Idefics）受益，而另一些模型（例如，Qwen）性能下降。为了解决这个问题，我们提出了一种用于微调MLLM的方向性推理注入（DRIFT）方法，这是一种轻量级方法，可在梯度空间中传递推理知识，而不会破坏多模态对齐。DRIFT预先计算推理先验，作为推理和多模态变体之间的参数空间差异，然后在多模态微调期间使用它来偏置梯度。这种方法保留了标准监督微调管道的简单性，同时实现了高效的推理转移。在包括MathVista和MathVerse在内的多模态推理基准上的大量实验表明，DRIFT始终优于朴素合并和监督微调，同时以一小部分成本匹配或超过了训练密集型方法。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型(MLLMs)推理能力不足的问题。现有方法，如大规模数据上的监督微调和强化学习，计算成本高昂。模型合并虽然是一种潜在的替代方案，但其效果在不同模型家族之间差异很大，有时甚至会降低性能。因此，需要一种高效且稳定的方法来提升MLLMs的推理能力。

**核心思路**：论文的核心思路是在梯度空间中注入方向性推理知识。具体来说，通过预先计算一个“推理先验”，该先验表示推理增强的LLM和多模态变体之间的参数空间差异。在多模态微调过程中，利用这个推理先验来偏置梯度，从而引导模型学习推理能力，同时保持多模态对齐。

**技术框架**：DRIFT方法主要包含以下几个阶段：
1. **推理先验计算**：首先，选择一个具有较强推理能力的LLM和一个多模态变体。计算这两个模型在参数空间上的差异，得到推理先验。
2. **多模态微调**：使用标准的多模态数据集对多模态模型进行微调。在计算梯度时，将推理先验引入梯度计算中，从而引导模型学习推理能力。
3. **模型评估**：在多模态推理基准上评估微调后的模型性能。

**关键创新**：DRIFT的关键创新在于：
1. **梯度空间注入**：不同于直接合并模型参数，DRIFT在梯度空间中注入推理知识，避免了参数冲突和模型不稳定问题。
2. **方向性推理**：通过预计算推理先验，明确了推理知识的方向，从而更有效地引导模型学习推理能力。
3. **轻量级**：DRIFT不需要额外的训练数据或复杂的训练策略，只需在标准微调过程中引入推理先验即可。

**关键设计**：
1. **推理先验的计算**：推理先验被定义为推理模型和多模态模型参数的差值，即 Δθ = θ_reasoning - θ_multimodal。
2. **梯度偏置**：在多模态微调过程中，梯度更新规则被修改为：θ = θ - η(∇L + λΔθ)，其中 η 是学习率，λ 是一个超参数，用于控制推理先验的影响程度。
3. **超参数λ的选择**：λ 的值需要根据具体任务和数据集进行调整，以平衡推理能力和多模态对齐。

## 📊 实验亮点

实验结果表明，DRIFT在MathVista和MathVerse等基准测试中，显著优于朴素模型合并和标准监督微调。例如，在MathVista上，DRIFT相较于Naive Merging提升了超过5%，并且在性能上可以匹配甚至超过需要大量训练资源的方法，同时显著降低了训练成本。

## 🎯 应用场景

DRIFT方法可广泛应用于各种需要多模态推理能力的场景，例如视觉问答、图像描述、机器人导航等。通过提升MLLMs的推理能力，可以提高这些应用在复杂环境下的性能和可靠性。该方法降低了推理能力迁移的成本，使得更多研究者和开发者能够构建更智能的多模态系统。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) are rapidly advancing, yet their reasoning ability often lags behind that of strong text-only counterparts. Existing methods to bridge this gap rely on supervised fine-tuning over large-scale multimodal reasoning data or reinforcement learning, both of which are resource-intensive. A promising alternative is model merging, which interpolates parameters between reasoning-enhanced LLMs and multimodal variants. However, our analysis shows that naive merging is not always a "free lunch": its effectiveness varies drastically across model families, with some (e.g., LLaVA, Idefics) benefiting while others (e.g., Qwen) suffer performance degradation. To address this, we propose Directional Reasoning Injection for Fine-Tuning (DRIFT) MLLMs, a lightweight method that transfers reasoning knowledge in the gradient space, without destabilizing multimodal alignment. DRIFT precomputes a reasoning prior as the parameter-space difference between reasoning and multimodal variants, then uses it to bias gradients during multimodal fine-tuning. This approach preserves the simplicity of standard supervised fine-tuning pipelines while enabling efficient reasoning transfer. Extensive experiments on multimodal reasoning benchmarks, including MathVista and MathVerse, demonstrate that DRIFT consistently improves reasoning performance over naive merging and supervised fine-tuning, while matching or surpassing training-heavy methods at a fraction of the cost.

