---
layout: default
title: "Observer, Not Player: Simulating Theory of Mind in LLMs through Game Observation"
---

# Observer, Not Player: Simulating Theory of Mind in LLMs through Game Observation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19210" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19210v1</a>
  <a href="https://arxiv.org/pdf/2512.19210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19210v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19210v1', 'Observer, Not Player: Simulating Theory of Mind in LLMs through Game Observation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jerry Wang, Ting Yiu Liu

**分类**: cs.AI

**发布日期**: 2025-12-22

**备注**: Accepted at NeurIPS Workshop on Foundations of Reasoning in Language Models and Workshop on Bridging Language, Agent, and World Model

---

## 💡 一句话要点

**提出基于观察者模式的框架，通过石头剪刀布游戏评估LLM的心理理论能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心理理论` `策略推理` `博弈论` `智能体建模`

## 📋 核心要点

1. 现有方法难以有效评估LLM在策略性环境中的“理解”能力，缺乏对顺序行为推理的深入探究。
2. 将LLM定位为观察者，通过分析其对石头剪刀布游戏策略的识别和推理，模拟心理理论。
3. 构建包含静态和动态策略的基准，并提出联合损失和策略识别率等指标，综合评估LLM的推理能力。

## 📝 摘要（中文）

本文提出了一个交互式框架，用于评估大型语言模型（LLM）在简单但具有策略性的环境中是否表现出真正的“理解”能力。以石头剪刀布（RPS）为例，尽管其表面上很简单，但需要顺序推理、适应和策略识别。该系统将LLM定位为观察者，其任务是识别正在使用的策略，并阐明这种判断背后的推理。目的不是测试对石头剪刀布本身的知识，而是探究模型是否可以表现出类似心智的关于顺序行为的推理。为了支持系统评估，我们提供了一个基准，该基准由静态策略和由良好提示规则指定的轻量级动态策略组成。我们使用三个互补信号来量化观察者的预测与实际策略对引起的真实分布之间的一致性：交叉熵、Brier分数和期望值（EV）差异。这些指标进一步集成到一个统一的分数中，即联合损失，该损失平衡了校准、灵敏度和收益对齐。连同策略识别率（SIR）指标，我们的框架不仅捕获了预测准确性，还捕获了模型是否可以稳定地识别正在使用的潜在策略。该演示强调了交互性、透明性和可重复性。用户可以实时调整LLM分布，可视化损失的演变，并直接检查推理片段，以识别失败发生的位置和原因。通过这样做，我们的系统为顺序游戏中类似心智的推理提供了一个实用且可解释的代理，从而深入了解了当前LLM推理的优势和局限性。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLM）是否具备类似人类的“心理理论”（Theory of Mind）能力，即理解他人意图和策略的能力。现有方法难以在策略性环境中有效评估LLM的这种能力，尤其是在需要顺序推理和策略适应的场景下。传统的知识问答或文本生成任务无法充分体现LLM在复杂交互中的策略理解能力。

**核心思路**：论文的核心思路是将LLM置于一个“观察者”的角色，让其观察两个智能体之间的策略性互动（例如石头剪刀布游戏），并尝试识别和解释这些智能体所使用的策略。通过分析LLM的预测和推理过程，可以评估其是否具备理解他人意图和策略的能力。这种方法模拟了人类通过观察他人行为来推断其心理状态的过程。

**技术框架**：该框架包含以下主要模块：1) 游戏环境：使用石头剪刀布游戏作为测试环境，该游戏简单但需要策略性思考。2) 策略生成器：生成静态和动态的石头剪刀布策略，作为智能体的行为模式。动态策略由预先设定的规则驱动，并由prompt进行控制。3) 观察者（LLM）：LLM作为观察者，接收游戏历史记录作为输入，并预测每个智能体下一步行动的概率分布。4) 评估指标：使用交叉熵、Brier分数和期望值差异等指标来量化LLM预测的准确性，并结合策略识别率（SIR）来评估LLM识别潜在策略的能力。这些指标被整合到一个统一的“联合损失”中，以平衡校准、灵敏度和收益对齐。

**关键创新**：该论文的关键创新在于：1) 将LLM置于“观察者”的角色，模拟心理理论的推理过程。2) 构建了一个包含静态和动态策略的基准，用于系统评估LLM的策略理解能力。3) 提出了联合损失和策略识别率等综合指标，用于全面评估LLM的预测准确性和策略识别能力。与现有方法相比，该方法更侧重于评估LLM在策略性互动中的推理能力，而不仅仅是知识记忆或文本生成。

**关键设计**：在策略生成方面，论文设计了静态策略（例如始终选择石头）和动态策略（例如根据对手的历史行为进行调整）。动态策略通过精心设计的prompt来控制，使得LLM可以观察到不同类型的策略行为。在评估指标方面，联合损失的设计旨在平衡预测的准确性（交叉熵和Brier分数）和收益对齐（期望值差异），从而更全面地评估LLM的策略理解能力。策略识别率（SIR）则用于衡量LLM是否能够稳定地识别正在使用的潜在策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19210v1/pic/early_round.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19210v1/pic/late_round.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19210v1/pic/pipeline.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLM在识别静态策略方面表现良好，但在处理动态策略时面临挑战。联合损失和策略识别率等指标能够有效区分不同LLM的策略理解能力。通过交互式演示，用户可以实时调整LLM的分布，并观察损失的变化，从而深入了解LLM推理的优势和局限性。具体性能数据和对比基线在论文中进行了详细展示。

## 🎯 应用场景

该研究的潜在应用领域包括：1) 评估和改进LLM在多智能体环境中的决策能力。2) 开发更具人情味的AI助手，能够理解用户的意图和偏好。3) 在安全领域，用于分析对手的策略和预测其行为。未来的影响在于，该研究可以推动LLM在复杂交互场景中的应用，并促进人机协作的进一步发展。

## 📄 摘要（原文）

> We present an interactive framework for evaluating whether large language models (LLMs) exhibit genuine "understanding" in a simple yet strategic environment. As a running example, we focus on Rock-Paper-Scissors (RPS), which, despite its apparent simplicity, requires sequential reasoning, adaptation, and strategy recognition. Our system positions the LLM as an Observer whose task is to identify which strategies are being played and to articulate the reasoning behind this judgment. The purpose is not to test knowledge of Rock-Paper-Scissors itself, but to probe whether the model can exhibit mind-like reasoning about sequential behavior. To support systematic evaluation, we provide a benchmark consisting of both static strategies and lightweight dynamic strategies specified by well-prompted rules. We quantify alignment between the Observer's predictions and the ground-truth distributions induced by actual strategy pairs using three complementary signals: Cross-Entropy, Brier score, and Expected Value (EV) discrepancy. These metrics are further integrated into a unified score, the Union Loss, which balances calibration, sensitivity, and payoff alignment. Together with a Strategy Identification Rate (SIR) metric, our framework captures not only predictive accuracy but also whether the model can stably identify the latent strategies in play. The demo emphasizes interactivity, transparency, and reproducibility. Users can adjust LLM distributions in real time, visualize losses as they evolve, and directly inspect reasoning snippets to identify where and why failures occur. In doing so, our system provides a practical and interpretable proxy for mind-like inference in sequential games, offering insights into both the strengths and limitations of current LLM reasoning.

