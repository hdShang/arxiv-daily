---
layout: default
title: Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection
---

# Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20140" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20140v1</a>
  <a href="https://arxiv.org/pdf/2512.20140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20140v1', 'Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyou Yin, Ceyao Zhang, Min Hu, Kai Chen

**分类**: cs.AI

**发布日期**: 2025-12-23

**备注**: 9 pages,3 figures

---

## 💡 一句话要点

**通过噪声注入增强即用型LLM的零样本时间序列预测能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `零样本学习` `大型语言模型` `噪声注入` `推理时增强`

## 📋 核心要点

1. 现有零样本时间序列预测方法依赖微调或对分布偏移敏感，限制了即用型LLM的直接应用。
2. 该论文提出在时间序列标记化前注入噪声，作为推理时增强，迫使LLM关注鲁棒的时间模式。
3. 实验表明，该方法在多个数据集上有效提升了零样本预测性能，并在新数据集上验证了无偏差性。

## 📝 摘要（中文）

大型语言模型(LLMs)已展现出作为零样本时间序列(TS)预测器的有效性。关键挑战在于将TS数据标记化为与LLMs预训练知识对齐的文本表示。现有工作通常依赖于微调专门的模块来弥合这一差距，而一种截然不同但具有挑战性的范例旨在利用真正的即用型LLMs，无需任何微调，仅依赖于数值序列的战略性标记化。这些完全冻结模型的性能对输入数据的文本表示非常敏感，因为它们的参数无法适应分布偏移。本文提出了一种简单而高效的策略来克服这种脆弱性：在标记化之前将噪声注入原始时间序列。这种非侵入性干预充当一种推理时增强形式，迫使冻结的LLM基于鲁棒的底层时间模式而不是表面的数值伪像进行外推。我们从理论上分析了这种现象，并通过各种基准测试验证了其有效性。值得注意的是，为了完全消除LLM预训练期间数据污染可能产生的偏差，我们引入了两个新颖的TS数据集，这些数据集不在所有使用的LLM的预训练范围内，并始终观察到性能的提高。这项研究为直接利用即用型LLM进行时间序列预测提供了进一步的步骤。

## 🔬 方法详解

**问题定义**：论文旨在解决直接利用预训练好的、未经任何微调的大型语言模型（LLMs）进行零样本时间序列预测时，模型性能对输入数据表示方式过于敏感的问题。现有方法要么需要对LLM进行微调，要么依赖于专门的模块，这限制了LLM的通用性和即用性。直接使用LLM时，由于其参数无法适应时间序列数据的分布偏移，预测结果往往不稳定。

**核心思路**：论文的核心思路是在将时间序列数据输入LLM之前，向原始数据中注入噪声。这种噪声注入可以看作是一种推理时的数据增强方法，它迫使LLM关注时间序列数据中更鲁棒、更本质的模式，而不是依赖于表面的数值特征。通过这种方式，可以提高LLM对不同数据表示方式的泛化能力，从而提升零样本预测的性能。

**技术框架**：该方法的核心流程包括以下几个步骤：1) 获取原始时间序列数据；2) 向时间序列数据中注入噪声；3) 将加噪后的时间序列数据进行标记化，转换为LLM可以理解的文本表示；4) 将文本表示输入到预训练的LLM中进行预测；5) 将LLM的输出转换回时间序列预测结果。整个框架的关键在于噪声注入策略，它在数据预处理阶段起到了至关重要的作用。

**关键创新**：该论文最重要的技术创新点在于提出了噪声注入作为一种简单而有效的推理时增强方法，用于提高即用型LLM在零样本时间序列预测中的鲁棒性。与现有方法相比，该方法无需对LLM进行任何微调，也无需引入额外的模块，而是通过对输入数据进行简单的处理，即可显著提升预测性能。这种方法的创新之处在于它充分利用了LLM的预训练知识，并通过噪声注入来引导LLM关注更本质的时间模式。

**关键设计**：论文中关于噪声注入的具体实现细节（例如噪声的类型、幅度等）以及时间序列数据的标记化方式是关键的设计选择。论文可能探讨了不同类型的噪声（例如高斯噪声、均匀噪声等）对预测性能的影响，并选择了最优的噪声类型和幅度。此外，时间序列数据的标记化方式也会影响LLM的性能，论文可能采用了某种特定的标记化策略，例如将时间序列数据转换为自然语言描述或使用特殊的token表示时间序列的数值。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20140v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20140v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20140v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在多个时间序列数据集上显著提升了零样本预测性能。为了验证方法的有效性和消除数据污染的潜在偏差，作者构建了两个全新的时间序列数据集，并在这些数据集上观察到了一致的性能提升。具体提升幅度未知，但强调了该方法的有效性和鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于金融、气象、交通等领域的时间序列预测。通过直接利用预训练的LLM，无需针对特定领域进行微调，即可快速部署时间序列预测模型，降低了开发成本和时间。该方法还有助于提高预测模型的鲁棒性和泛化能力，使其能够更好地适应不同的数据分布和场景。未来，该方法有望成为一种通用的时间序列预测解决方案。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated effectiveness as zero-shot time series (TS) forecasters. The key challenge lies in tokenizing TS data into textual representations that align with LLMs' pre-trained knowledge. While existing work often relies on fine-tuning specialized modules to bridge this gap, a distinct, yet challenging, paradigm aims to leverage truly off-the-shelf LLMs without any fine-tuning whatsoever, relying solely on strategic tokenization of numerical sequences. The performance of these fully frozen models is acutely sensitive to the textual representation of the input data, as their parameters cannot adapt to distribution shifts. In this paper, we introduce a simple yet highly effective strategy to overcome this brittleness: injecting noise into the raw time series before tokenization. This non-invasive intervention acts as a form of inference-time augmentation, compelling the frozen LLM to extrapolate based on robust underlying temporal patterns rather than superficial numerical artifacts. We theoretically analyze this phenomenon and empirically validate its effectiveness across diverse benchmarks. Notably, to fully eliminate potential biases from data contamination during LLM pre-training, we introduce two novel TS datasets that fall outside all utilized LLMs' pre-training scopes, and consistently observe improved performance. This study provides a further step in directly leveraging off-the-shelf LLMs for time series forecasting.

