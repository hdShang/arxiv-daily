---
layout: default
title: This Time is Different: An Observability Perspective on Time Series Foundation Models
---

# This Time is Different: An Observability Perspective on Time Series Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14766" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14766v2</a>
  <a href="https://arxiv.org/pdf/2505.14766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14766v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14766v2', 'This Time is Different: An Observability Perspective on Time Series Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ben Cohen, Emaad Khwaja, Youssef Doubli, Salahidine Lemaachi, Chris Lettieri, Charles Masson, Hugo Miccinilli, Elise Ramé, Qiqi Ren, Afshin Rostamizadeh, Jean Ogier du Terrail, Anna-Monica Toon, Kan Wang, Stephan Xie, Zongzhe Xu, Viktoriya Zhukova, David Asker, Ameet Talwalkar, Othmane Abou-Amal

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-11-04)

**🔗 代码/项目**: [GITHUB](https://github.com/DataDog/toto) | [HUGGINGFACE](https://huggingface.co/Datadog/Toto-Open-Base-1.0)

---

## 💡 一句话要点

**提出Toto模型以解决多变量可观测时间序列预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `多变量数据` `可观测性` `深度学习` `模型训练` `基准评估` `开源`

## 📋 核心要点

1. 现有时间序列预测模型在处理多变量可观测数据时面临诸多挑战，尤其是在数据规模和多样性方面。
2. Toto模型通过现代解码器架构和针对可观测数据的创新设计，提升了多变量时间序列的预测能力。
3. 实验结果表明，Toto在BOOM基准和其他通用时间序列预测基准上均取得了最先进的性能，显著提升了预测准确性。

## 📝 摘要（中文）

我们介绍了Toto，一个具有1.51亿参数的时间序列预测基础模型。Toto采用现代解码器架构，并结合针对多变量可观测时间序列数据特定挑战的架构创新。Toto的预训练语料库由可观测数据、开放数据集和合成数据混合而成，规模是领先时间序列基础模型的4-10倍。此外，我们还引入了BOOM，一个包含2,807个真实时间序列的规模庞大的基准数据集，包含3.5亿个观测值。Toto在BOOM和已建立的通用时间序列预测基准上均表现出色，达到了最先进的性能。Toto的模型权重、推理代码和评估脚本，以及BOOM的数据和评估代码，均以Apache 2.0许可证开源，访问链接为https://huggingface.co/Datadog/Toto-Open-Base-1.0和https://github.com/DataDog/toto。

## 🔬 方法详解

**问题定义**：本论文旨在解决多变量可观测时间序列预测中的数据规模和多样性不足的问题。现有模型在处理复杂的多变量数据时，往往无法充分利用数据的潜在信息，导致预测性能不佳。

**核心思路**：Toto模型通过引入现代解码器架构，并结合针对可观测数据的特定设计，旨在提升模型对多变量时间序列的理解和预测能力。这样的设计使得模型能够更好地捕捉时间序列中的复杂模式和关系。

**技术框架**：Toto的整体架构包括数据预处理、模型训练和评估三个主要阶段。首先，模型使用多种来源的数据进行预训练，包括可观测数据和开放数据集。其次，采用解码器架构进行时间序列的建模，最后通过BOOM基准进行评估。

**关键创新**：Toto的主要创新在于其大规模的预训练语料库和针对可观测数据的架构设计。与现有模型相比，Toto在数据处理和模型架构上进行了优化，使其在多变量时间序列预测中表现出色。

**关键设计**：Toto的模型参数设置经过精心调整，采用了适合多变量时间序列的损失函数和网络结构，确保模型能够有效地学习时间序列中的复杂关系。

## 📊 实验亮点

Toto在BOOM基准上表现出色，达到了最先进的性能，具体而言，其在350万观测值的评估中相较于现有基线模型提升了显著的预测准确性。这一成果证明了Toto在处理复杂多变量时间序列数据方面的有效性。

## 🎯 应用场景

Toto模型在多种领域具有广泛的应用潜力，包括金融市场预测、设备故障检测和智能制造等。其强大的预测能力能够帮助企业更好地进行决策，优化资源配置，提高运营效率。未来，Toto的设计理念和方法可以推广到其他类型的时间序列分析任务中，推动相关领域的发展。

## 📄 摘要（原文）

> We introduce Toto, a time series forecasting foundation model with 151 million parameters. Toto uses a modern decoder-only architecture coupled with architectural innovations designed to account for specific challenges found in multivariate observability time series data. Toto's pre-training corpus is a mixture of observability data, open datasets, and synthetic data, and is 4-10$\times$ larger than those of leading time series foundation models. Additionally, we introduce BOOM, a large-scale benchmark consisting of 350 million observations across 2,807 real-world time series. For both Toto and BOOM, we source observability data exclusively from Datadog's own telemetry and internal observability metrics. Extensive evaluations demonstrate that Toto achieves state-of-the-art performance on both BOOM and on established general purpose time series forecasting benchmarks. Toto's model weights, inference code, and evaluation scripts, as well as BOOM's data and evaluation code, are all available as open source under the Apache 2.0 License available at https://huggingface.co/Datadog/Toto-Open-Base-1.0 and https://github.com/DataDog/toto.

