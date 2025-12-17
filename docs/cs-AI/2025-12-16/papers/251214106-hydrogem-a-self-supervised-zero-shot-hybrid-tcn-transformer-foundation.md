---
layout: default
title: HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14106" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14106</a>
  <a href="https://arxiv.org/pdf/2512.14106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14106" onclick="toggleFavorite(this, '2512.14106', 'HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ijaz Ul Haq, Byung Suk Lee, Julia N. Perdrial, David Baude

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**HydroGEM：用于洲际尺度流量质量控制的自监督零样本混合TCN-Transformer基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流量质量控制` `自监督学习` `时间卷积网络` `Transformer` `水文模型` `零样本学习` `异常检测`

## 📋 核心要点

1. 现有流量监测网络数据质量维护依赖人工，成本高昂，缺乏自动化手段。
2. HydroGEM通过自监督学习水文表征，并利用混合TCN-Transformer架构捕获时间依赖关系，实现流量质量控制。
3. 实验表明，HydroGEM在流量异常检测和重建方面显著优于现有方法，并具备跨国泛化能力。

## 📝 摘要（中文）

实时流量监测网络每年产生数百万条观测数据，但维护数千个远程传感器的数据质量仍然非常耗费人力。我们提出了HydroGEM（用于监测的水文可泛化编码器），这是一个用于洲际尺度流量质量控制的基础模型。HydroGEM使用两阶段训练：在来自3724个美国地质调查局站点的603万个序列上进行自监督预训练，以学习水文表示，然后使用合成异常进行微调，以进行检测和重建。混合TCN-Transformer架构（1420万个参数）捕获局部时间模式和长期依赖关系，而分层归一化处理六个数量级的流量。在包含799个站点和18种专家验证的异常类型的保留合成测试中，HydroGEM在检测方面实现了F1 = 0.792，重建误差降低了68.7％，比现有方法提高了36.3％。零样本迁移到100个加拿大环境与气候变化部站点，产生F1 = 0.586，超过了所有基线，并证明了跨国泛化能力。该模型在校正幅度上保持一致的检测，并与运营季节性模式保持一致。HydroGEM专为人工参与的工作流程而设计——输出是需要专家审查的质量控制建议，而不是自主校正。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模流量监测网络中数据质量控制的问题。现有方法依赖人工，效率低下且成本高昂。缺乏能够自动检测和纠正流量数据异常的模型，尤其是在跨区域和跨国界的情况下。

**核心思路**：论文的核心思路是利用自监督学习方法，从大量的无标签流量数据中学习水文表征。然后，通过在合成异常数据上进行微调，使模型能够检测和重建真实的流量异常。混合TCN-Transformer架构旨在同时捕获局部时间模式和长期依赖关系，从而提高异常检测的准确性。

**技术框架**：HydroGEM的整体框架包含两个主要阶段：1) 自监督预训练阶段：使用大量的USGS流量数据进行预训练，学习水文表征。2) 微调阶段：使用合成的流量异常数据进行微调，提高模型对异常的检测和重建能力。模型的核心是一个混合TCN-Transformer架构，用于提取流量数据的时间特征。

**关键创新**：HydroGEM的关键创新点在于：1) 提出了一个用于流量质量控制的自监督基础模型。2) 使用混合TCN-Transformer架构，能够同时捕获局部和全局的时间依赖关系。3) 采用分层归一化方法，处理不同站点流量数据量级差异大的问题。4) 实现了零样本跨国迁移，无需目标域数据进行训练。

**关键设计**：HydroGEM使用了混合TCN-Transformer架构，其中TCN用于捕获局部时间模式，Transformer用于捕获长期依赖关系。分层归一化用于处理不同站点流量数据量级差异大的问题。损失函数包括检测损失和重建损失，用于优化模型的异常检测和重建能力。模型参数量为1420万。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HydroGEM在合成测试集上实现了F1=0.792的异常检测性能，重建误差降低了68.7%，相比现有方法提升了36.3%。在零样本跨国迁移到加拿大站点时，F1值达到0.586，超过所有基线模型，验证了模型的泛化能力。该模型在不同异常幅度下保持稳定的检测性能，并与实际的季节性模式相符。

## 🎯 应用场景

HydroGEM可应用于大规模流量监测网络的数据质量控制，提高数据质量和可靠性，减少人工干预，降低维护成本。该模型还可用于水资源管理、洪水预警、气候变化研究等领域，为相关决策提供支持。未来，该模型有望扩展到其他类型的水文数据，例如地下水位、水质等。

## 📄 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.

