---
layout: default
title: "HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control"
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14106" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14106v1</a>
  <a href="https://arxiv.org/pdf/2512.14106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14106v1', 'HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ijaz Ul Haq, Byung Suk Lee, Julia N. Perdrial, David Baude

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Supplementary materials, datasets, and implementation code will be made publicly available upon acceptance for publication in a peer-reviewed journal

---

## 💡 一句话要点

**HydroGEM：用于洲际尺度流量质量控制的自监督零样本混合TCN-Transformer基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流量质量控制` `自监督学习` `时间卷积网络` `Transformer` `水文模型` `异常检测` `零样本学习`

## 📋 核心要点

1. 现有流量监测网络数据质量维护耗时费力，缺乏有效自动化方法。
2. HydroGEM通过自监督学习水文表征，并使用混合TCN-Transformer架构进行异常检测和重建。
3. 实验表明，HydroGEM在流量异常检测和重建方面显著优于现有方法，并具备跨国泛化能力。

## 📝 摘要（中文）

实时流量监测网络每年产生数百万条观测数据，但维护数千个远程传感器的数据质量仍然非常耗费人力。我们提出了HydroGEM（用于监测的水文可泛化编码器），这是一个用于洲际尺度流量质量控制的基础模型。HydroGEM使用两阶段训练：在来自3724个美国地质调查局（USGS）站点的603万个序列上进行自监督预训练，以学习水文表征，然后使用合成异常进行微调，以进行检测和重建。混合TCN-Transformer架构（1420万个参数）捕获局部时间模式和长期依赖关系，而分层归一化处理六个数量级的流量。在包含799个站点和18种专家验证的异常类型的保留合成测试中，HydroGEM在检测方面实现了F1 = 0.792，重建误差降低了68.7％，比现有方法提高了36.3％。零样本迁移到100个加拿大环境与气候变化部（Environment and Climate Change Canada）站点，产生F1 = 0.586，超过了所有基线，并证明了跨国泛化能力。该模型在校正幅度上保持一致的检测，并与运营季节性模式保持一致。HydroGEM专为人工参与的工作流程而设计——输出是需要专家审查的质量控制建议，而不是自主校正。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模流量监测数据中的质量控制问题，特别是异常检测和数据修复。现有方法通常依赖于人工检查，效率低下且难以扩展到洲际尺度。此外，现有方法在处理不同量级流量数据和跨区域泛化方面存在局限性。

**核心思路**：论文的核心思路是利用自监督学习从大量无标签流量数据中学习水文表征，然后利用这些表征进行异常检测和重建。通过预训练-微调的两阶段训练策略，模型能够有效地捕捉流量数据中的时间依赖关系和量级差异，并具备良好的泛化能力。

**技术框架**：HydroGEM采用两阶段训练框架。第一阶段，模型在大量USGS流量数据上进行自监督预训练，学习水文表征。第二阶段，模型使用合成异常数据进行微调，以提高异常检测和重建的性能。模型采用混合TCN-Transformer架构，其中TCN用于捕捉局部时间模式，Transformer用于捕捉长期依赖关系。此外，模型还采用了分层归一化方法，以处理不同量级的流量数据。

**关键创新**：HydroGEM的关键创新在于以下几点：1) 提出了一个用于洲际尺度流量质量控制的基础模型；2) 采用了自监督学习和混合TCN-Transformer架构；3) 提出了分层归一化方法，以处理不同量级的流量数据。与现有方法相比，HydroGEM能够更有效地进行异常检测和重建，并具备更好的泛化能力。

**关键设计**：HydroGEM的关键设计包括：1) 混合TCN-Transformer架构，其中TCN的卷积核大小和Transformer的注意力头数需要仔细调整；2) 分层归一化方法，其具体实现方式需要根据流量数据的量级分布进行调整；3) 自监督预训练的目标函数，例如采用重建误差或对比学习等方法；4) 合成异常数据的生成方法，需要尽可能覆盖各种类型的异常情况。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14106v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HydroGEM在保留的合成测试中，异常检测F1值达到0.792，重建误差降低68.7%，相比现有方法提升36.3%。零样本迁移到加拿大站点，F1值达到0.586，超过所有基线模型，展示了良好的跨国泛化能力。实验结果表明，HydroGEM在流量异常检测和重建方面具有显著优势。

## 🎯 应用场景

HydroGEM可应用于大规模流量监测网络的质量控制，提高数据质量和监测效率。该模型可用于自动检测和修复流量数据中的异常，减少人工干预，并为水资源管理、气候变化研究和灾害预警等领域提供更可靠的数据支持。未来，该模型可扩展到其他类型的水文数据，例如地下水位和水质数据。

## 📄 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.

