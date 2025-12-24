---
layout: default
title: Output Scaling: YingLong-Delayed Chain of Thought in a Large Pretrained Time Series Forecasting Model
---

# Output Scaling: YingLong-Delayed Chain of Thought in a Large Pretrained Time Series Forecasting Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11029" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11029v1</a>
  <a href="https://arxiv.org/pdf/2506.11029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11029v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11029v1', 'Output Scaling: YingLong-Delayed Chain of Thought in a Large Pretrained Time Series Forecasting Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xue Wang, Tian Zhou, Jinyang Gao, Bolin Ding, Jingren Zhou

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-20

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/qcw1314/YingLong_300m)

---

## 💡 一句话要点

**提出YingLong框架以提升时间序列预测精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `非因果模型` `双向注意力` `延迟思维链` `多输入集成` `模型评估` `深度学习`

## 📋 核心要点

1. 现有时间序列预测方法多采用直接或递归方式，存在准确性不足的问题。
2. 论文提出了一种非因果的双向注意力编码器YingLong，通过延迟思维链推理提升预测精度。
3. 实验结果显示，YingLong在多个数据集上超越了现有模型，最佳性能超过60%，并在GIFT-Eval基准中表现优异。

## 📝 摘要（中文）

我们提出了一种时间序列预测的联合预测框架，与传统的直接或递归方法形成对比。该框架在我们设计的基础模型YingLong上实现了最先进的性能，并揭示了一种新的缩放效应：更长的输出显著提高了模型的准确性，这得益于我们非因果方法中的延迟思维链推理。YingLong是一个非因果的双向注意力编码器，仅使用变换器结构，通过掩码令牌恢复进行训练，更有效地与语言理解任务对齐。此外，我们通过多输入集成来解决输出方差，从而提升性能。我们发布了四个基础模型，参数范围从6M到300M，在ETT和Weather数据集的零-shot任务中表现优越，YingLong的最佳性能超过60%。为确保模型的通用性，我们使用GIFT-Eval基准评估模型，该基准包含7个领域的23个时间序列数据集。YingLong显著超越了最佳时间序列基础模型和端到端训练模型，分别提高了14%和44%的排名。预训练的300M模型可在https://huggingface.co/qcw1314/YingLong_300m获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统时间序列预测方法在准确性和灵活性上的不足，尤其是直接和递归方法的局限性。现有方法往往无法有效处理复杂的时间依赖关系，导致预测性能不佳。

**核心思路**：我们提出的YingLong框架采用非因果的双向注意力机制，通过延迟思维链推理来增强模型的预测能力。该方法允许模型在生成输出时考虑更长的上下文，从而提高准确性。

**技术框架**：YingLong的整体架构包括一个编码器部分，使用双向注意力机制进行信息处理，并通过掩码令牌恢复进行训练。我们还引入了多输入集成策略，以减少输出的方差并提升性能。

**关键创新**：YingLong的主要创新在于其非因果的设计和延迟思维链推理，这与现有的因果模型形成鲜明对比。通过这种设计，模型能够更好地理解和处理时间序列数据中的复杂关系。

**关键设计**：在模型设计中，我们设置了不同规模的参数（6M至300M），并采用了适合时间序列预测的损失函数。模型通过多输入集成来优化输出的稳定性和准确性。

## 📊 实验亮点

实验结果表明，YingLong在ETT和Weather数据集的零-shot任务中表现优越，最佳性能超过60%。此外，在GIFT-Eval基准测试中，YingLong相比于最佳时间序列基础模型和端到端训练模型，分别提高了14%和44%的排名，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场预测、气象数据分析以及供应链管理等时间序列相关的任务。YingLong框架的高准确性和灵活性使其在实际应用中具有重要价值，能够为决策提供更可靠的支持。未来，该模型可能推动更多领域的时间序列分析研究，提升智能决策系统的性能。

## 📄 摘要（原文）

> We present a joint forecasting framework for time series prediction that contrasts with traditional direct or recursive methods. This framework achieves state-of-the-art performance for our designed foundation model, YingLong, and reveals a novel scaling effect: longer outputs significantly enhance model accuracy due to delayed chain-of-thought reasoning in our non-causal approach. YingLong is a non-causal, bidirectional attention encoder-only transformer trained through masked token recovery, aligning more effectively with language understanding tasks than with generation tasks. Additionally, we boost performance by tackling output variance with a multi-input ensemble. We release four foundation models ranging from 6M to 300M parameters, demonstrating superior results in zero-shot tasks on the ETT and Weather datasets. YingLong achieves more than 60% best performance. To ensure generalizability, we assessed the models using the GIFT-Eval benchmark, which comprises 23 time series datasets across 7 domains. Yinglong significantly outperformed the best time-series foundation models, end-to-end trained models by 14% and 44% in rank respectively.The pretrained 300M model is available at https://huggingface.co/qcw1314/YingLong_300m

