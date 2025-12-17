---
layout: default
title: SimCast: Enhancing Precipitation Nowcasting with Short-to-Long Term Knowledge Distillation
---

# SimCast: Enhancing Precipitation Nowcasting with Short-to-Long Term Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07953" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07953v1</a>
  <a href="https://arxiv.org/pdf/2510.07953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07953v1" onclick="toggleFavorite(this, '2510.07953v1', 'SimCast: Enhancing Precipitation Nowcasting with Short-to-Long Term Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifang Yin, Shengkai Chen, Yiyao Li, Lu Wang, Ruibing Jin, Wei Cui, Shili Xiang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-09

**备注**: accepted by ICME 2025

**期刊**: IEEE International Conference on Multimedia and Expo (ICME) 2025

---

## 💡 一句话要点

**SimCast：利用短时到长时知识蒸馏增强降水临近预报**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `降水临近预报` `知识蒸馏` `短时到长时预测` `加权MSE损失` `扩散模型` `确定性预测` `概率模型`

## 📋 核心要点

1. 现有临近预报方法难以兼顾短时和长时预测的准确性，尤其是在强降雨区域。
2. SimCast通过短时到长时的知识蒸馏，并结合加权MSE损失，提升模型对强降雨区域的预测能力。
3. 实验表明，SimCast在多个数据集上显著优于现有方法，CSI指标提升明显。

## 📝 摘要（中文）

降水临近预报是一项极具挑战性的任务，它基于当前观测预测未来的雷达序列，其难度源于地球系统固有的复杂性。准确的临近预报对于应对各种社会需求至关重要，包括灾害管理、农业、交通运输和能源优化。作为现有非自回归临近预报方法的补充，我们研究了预测范围对临近预报模型的影响，并提出了SimCast，一种新颖的训练流程，其特点是短时到长时知识蒸馏技术，并结合加权MSE损失来优先考虑强降雨区域。无需在推理过程中引入额外的开销即可获得改进的临近预报。由于SimCast生成确定性预测，我们进一步将其集成到名为CasCast的基于扩散的框架中，利用概率模型的优势来克服确定性输出中的模糊性和分布偏移等限制。在三个基准数据集上的大量实验结果验证了所提出框架的有效性，在SEVIR、HKO-7和MeteoNet上分别实现了0.452、0.474和0.361的平均CSI分数，显著优于现有方法。

## 🔬 方法详解

**问题定义**：降水临近预报旨在根据当前雷达观测数据预测未来一段时间内的降水情况。现有方法，特别是确定性预测模型，在长时预测中容易出现模糊性和分布偏移问题，难以准确预测强降雨区域。同时，如何有效利用不同预测时间尺度的信息也是一个挑战。

**核心思路**：SimCast的核心思路是利用短时预测的准确性来指导长时预测，通过知识蒸馏的方式将短时预测模型的知识迁移到长时预测模型。同时，通过加权MSE损失，更加关注强降雨区域的预测精度。这种方法旨在提高长时预测的清晰度和准确性，尤其是在关键的强降雨区域。

**技术框架**：SimCast的训练流程包含两个主要部分：首先，训练一个短时预测模型（Teacher模型），使其能够准确预测短时间内的降水情况。然后，利用该Teacher模型的预测结果作为监督信号，训练一个长时预测模型（Student模型）。Student模型通过学习Teacher模型的输出，从而获得更准确的长时预测能力。此外，SimCast还集成了CasCast，这是一个基于扩散模型的框架，用于进一步提升预测结果的质量，克服确定性预测的局限性。

**关键创新**：SimCast的关键创新在于其短时到长时的知识蒸馏策略。与传统的知识蒸馏方法不同，SimCast特别关注不同预测时间尺度之间的知识迁移。通过将短时预测的知识传递给长时预测模型，SimCast能够有效地提高长时预测的准确性和清晰度。此外，加权MSE损失的引入使得模型更加关注强降雨区域的预测，进一步提升了模型在关键区域的性能。

**关键设计**：SimCast使用MSE损失函数的加权版本，对强降雨区域赋予更高的权重，促使模型更加关注这些区域的预测。具体的权重分配策略可能依赖于降水强度。此外，Teacher和Student模型的具体网络结构选择未明确说明，但可以根据具体任务选择合适的卷积神经网络或其他时序模型。CasCast框架则利用扩散模型生成更逼真的降水预测结果，具体实现细节未知。

## 📊 实验亮点

SimCast在SEVIR、HKO-7和MeteoNet三个基准数据集上取得了显著的性能提升，平均CSI分数分别达到0.452、0.474和0.361，大幅超越了现有方法。这表明SimCast在实际应用中具有很强的竞争力，能够提供更准确、可靠的降水临近预报。

## 🎯 应用场景

SimCast可应用于灾害预警、农业生产、交通调度和能源优化等领域。准确的降水临近预报能够帮助政府和相关机构提前做好防灾减灾准备，减少自然灾害带来的损失。在农业方面，可以指导农民合理安排灌溉和施肥，提高农作物产量。在交通领域，可以为交通管理者提供决策支持，保障交通安全。在能源领域，可以帮助优化水电站的发电调度。

## 📄 摘要（原文）

> Precipitation nowcasting predicts future radar sequences based on current observations, which is a highly challenging task driven by the inherent complexity of the Earth system. Accurate nowcasting is of utmost importance for addressing various societal needs, including disaster management, agriculture, transportation, and energy optimization. As a complementary to existing non-autoregressive nowcasting approaches, we investigate the impact of prediction horizons on nowcasting models and propose SimCast, a novel training pipeline featuring a short-to-long term knowledge distillation technique coupled with a weighted MSE loss to prioritize heavy rainfall regions. Improved nowcasting predictions can be obtained without introducing additional overhead during inference. As SimCast generates deterministic predictions, we further integrate it into a diffusion-based framework named CasCast, leveraging the strengths from probabilistic models to overcome limitations such as blurriness and distribution shift in deterministic outputs. Extensive experimental results on three benchmark datasets validate the effectiveness of the proposed framework, achieving mean CSI scores of 0.452 on SEVIR, 0.474 on HKO-7, and 0.361 on MeteoNet, which outperforms existing approaches by a significant margin.

