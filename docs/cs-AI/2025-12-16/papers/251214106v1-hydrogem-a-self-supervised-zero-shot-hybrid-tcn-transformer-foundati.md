---
layout: default
title: HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14106" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14106v1</a>
  <a href="https://arxiv.org/pdf/2512.14106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14106v1" onclick="toggleFavorite(this, '2512.14106v1', 'HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control')" title="添加到收藏夹">☆ 收藏</button>
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

**关键词**: `流量质量控制` `自监督学习` `时间序列预测` `TCN-Transformer` `基础模型`

## 📋 核心要点

1. 现有流量监测网络数据质量维护依赖大量人工，缺乏自动化和泛化能力。
2. HydroGEM通过自监督预训练和合成异常微调，学习水文表示，实现流量质量控制。
3. 实验表明，HydroGEM在流量异常检测和重建方面显著优于现有方法，并具备跨国泛化能力。

## 📝 摘要（中文）

实时流量监测网络每年产生数百万条观测数据，但维护数千个远程传感器的数据质量仍然需要大量人工。我们提出了HydroGEM（用于监测的水文可泛化编码器），这是一个用于洲际尺度流量质量控制的基础模型。HydroGEM使用两阶段训练：在来自3724个USGS站点的603万个序列上进行自监督预训练，以学习水文表示，然后使用合成异常进行微调，以进行检测和重建。混合TCN-Transformer架构（1420万个参数）捕获局部时间模式和长期依赖关系，而分层归一化处理六个数量级的流量。在包含799个站点和18种专家验证的异常类型的保留合成测试中，HydroGEM在检测方面实现了F1 = 0.792，重建误差降低了68.7%，比现有方法提高了36.3%。零样本迁移到100个加拿大环境与气候变化部站点，产生F1 = 0.586，超过所有基线，证明了跨国泛化能力。该模型在校正幅度上保持一致的检测，并与运营季节性模式对齐。HydroGEM专为人工参与的工作流程而设计——输出是需要专家审查的质量控制建议，而不是自主校正。

## 🔬 方法详解

**问题定义**：论文旨在解决洲际尺度下，实时流量监测网络中大量传感器数据质量控制问题。现有方法依赖人工，效率低且难以泛化到新的区域或数据集。缺乏能够自动检测和修复流量数据异常的模型。

**核心思路**：论文的核心思路是利用自监督学习方法，从大量无标签的流量数据中学习水文表示，然后通过在合成异常数据上进行微调，使模型具备检测和重建流量异常的能力。这种方法避免了对大量标注数据的依赖，提高了模型的泛化能力。

**技术框架**：HydroGEM采用两阶段训练框架。第一阶段是自监督预训练，使用来自USGS站点的603万个流量序列，通过某种自监督学习任务（具体任务未知）学习水文表示。第二阶段是微调，使用合成的流量异常数据，训练模型进行异常检测和重建。模型采用混合TCN-Transformer架构，结合了TCN捕获局部时间模式的能力和Transformer捕获长期依赖关系的能力。

**关键创新**：HydroGEM的关键创新在于：1) 提出了一个用于流量质量控制的自监督基础模型；2) 采用了混合TCN-Transformer架构，能够同时捕获局部和长期的时间依赖关系；3) 使用分层归一化方法，处理不同站点流量数量级差异大的问题。

**关键设计**：HydroGEM模型包含1420万个参数。混合TCN-Transformer架构的具体细节（如TCN和Transformer的层数、参数等）未知。分层归一化的具体实现方式未知。损失函数的设计也未知，但可能包括异常检测的分类损失和异常重建的回归损失。

## 📊 实验亮点

HydroGEM在合成异常测试中，异常检测F1值达到0.792，重建误差降低68.7%，相比现有方法提升36.3%。在零样本迁移到加拿大站点时，F1值达到0.586，超过所有基线模型，展示了良好的跨国泛化能力。模型在不同校正幅度下保持一致的检测性能，并与季节性模式对齐。

## 🎯 应用场景

HydroGEM可应用于大规模流量监测网络的数据质量控制，减少人工干预，提高数据质量和可用性。该模型可用于水资源管理、洪水预警、气候变化研究等领域，为相关决策提供更可靠的数据支持。未来，该模型可扩展到其他水文变量，如水位、水质等，构建更全面的水文监测系统。

## 📄 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.

