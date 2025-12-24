---
layout: default
title: "From Forecasting to Planning: Policy World Model for Collaborative State-Action Prediction"
---

# From Forecasting to Planning: Policy World Model for Collaborative State-Action Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19654" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19654v2</a>
  <a href="https://arxiv.org/pdf/2510.19654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19654v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19654v2', 'From Forecasting to Planning: Policy World Model for Collaborative State-Action Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhida Zhao, Talas Fu, Yifan Wang, Lijun Wang, Huchuan Lu

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-10-22 (更新: 2025-11-25)

**备注**: Accepted by NuerIPS 2025 (Poster)

**🔗 代码/项目**: [GITHUB](https://github.com/6550Zhao/Policy-World-Model)

---

## 💡 一句话要点

**提出策略世界模型PWM，用于协同状态-动作预测，提升自动驾驶规划能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `轨迹规划` `自动驾驶` `状态预测` `动作预测` `Transformer` `策略学习`

## 📋 核心要点

1. 现有世界模型主要用于世界模拟，与轨迹规划脱钩，未能充分发挥其在自动驾驶系统中的潜力。
2. PWM通过协同状态-动作预测，模拟人类的预期感知，利用学习到的世界知识来提升规划性能。
3. PWM采用动态增强的并行token生成机制，提高了视频预测效率，仅使用前置摄像头就超越了多视角/模态方法。

## 📝 摘要（中文）

本文提出了一种新的自动驾驶范式，名为策略世界模型（PWM）。该模型将世界建模和轨迹规划集成在一个统一的架构中，并通过提出的无动作未来状态预测方案，利用学习到的世界知识来促进规划。通过协同状态-动作预测，PWM能够模仿类人化的预期感知，从而产生更可靠的规划性能。为了提高视频预测的效率，本文进一步引入了一种动态增强的并行token生成机制，配备了上下文引导的tokenizer和自适应动态焦点损失。仅使用前置摄像头输入，该方法就能达到或超过依赖多视角和多模态输入的state-of-the-art方法。

## 🔬 方法详解

**问题定义**：现有自动驾驶世界模型通常与轨迹规划分离，导致规划性能受限。虽然一些工作尝试统一世界建模和规划，但世界建模对规划的促进机制仍需深入研究。现有方法通常依赖多视角或多模态输入，成本较高。

**核心思路**：本文的核心在于提出一种策略世界模型（PWM），将世界建模和轨迹规划整合到一个统一的框架中。PWM通过学习环境的动态模型，预测未来状态，并利用这些预测来指导轨迹规划。通过协同状态-动作预测，模型能够学习到更丰富的环境信息，从而提高规划的可靠性。

**技术框架**：PWM包含三个主要模块：状态编码器、策略网络和世界模型。状态编码器将当前状态信息编码为潜在向量。策略网络根据潜在向量生成动作序列。世界模型根据当前状态和动作序列预测未来的状态。整个框架通过端到端的方式进行训练，以最小化预测状态和真实状态之间的差异。

**关键创新**：PWM的关键创新在于其协同状态-动作预测机制和动态增强的并行token生成机制。协同状态-动作预测使得模型能够同时学习状态和动作之间的关系，从而提高预测的准确性。动态增强的并行token生成机制提高了视频预测的效率，使得模型能够处理更长的视频序列。

**关键设计**：PWM使用Transformer架构作为其核心组件。状态编码器和世界模型都基于Transformer。为了提高训练效率，本文引入了一种自适应动态焦点损失，该损失函数能够更加关注难以预测的状态。动态增强的并行token生成机制包含一个上下文引导的tokenizer和一个自适应动态焦点损失。

## 📊 实验亮点

实验结果表明，PWM在自动驾驶场景下取得了显著的性能提升。仅使用前置摄像头输入，PWM的性能就能够匹配甚至超过依赖多视角和多模态输入的state-of-the-art方法。这表明PWM能够有效地利用学习到的世界知识来指导规划，并具有很强的泛化能力。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航等领域。通过学习环境的动态模型，系统能够更好地理解周围环境，并做出更合理的决策。该方法仅依赖前置摄像头输入，降低了硬件成本，具有广泛的应用前景。未来可进一步扩展到更复杂的环境和任务中。

## 📄 摘要（原文）

> Despite remarkable progress in driving world models, their potential for autonomous systems remains largely untapped: the world models are mostly learned for world simulation and decoupled from trajectory planning. While recent efforts aim to unify world modeling and planning in a single framework, the synergistic facilitation mechanism of world modeling for planning still requires further exploration. In this work, we introduce a new driving paradigm named Policy World Model (PWM), which not only integrates world modeling and trajectory planning within a unified architecture, but is also able to benefit planning using the learned world knowledge through the proposed action-free future state forecasting scheme. Through collaborative state-action prediction, PWM can mimic the human-like anticipatory perception, yielding more reliable planning performance. To facilitate the efficiency of video forecasting, we further introduce a dynamically enhanced parallel token generation mechanism, equipped with a context-guided tokenizer and an adaptive dynamic focal loss. Despite utilizing only front camera input, our method matches or exceeds state-of-the-art approaches that rely on multi-view and multi-modal inputs. Code and model weights will be released at https://github.com/6550Zhao/Policy-World-Model.

