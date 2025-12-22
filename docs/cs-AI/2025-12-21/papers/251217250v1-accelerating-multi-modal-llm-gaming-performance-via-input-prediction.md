---
layout: default
title: Accelerating Multi-modal LLM Gaming Performance via Input Prediction and Mishit Correction
---

# Accelerating Multi-modal LLM Gaming Performance via Input Prediction and Mishit Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17250" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17250v1</a>
  <a href="https://arxiv.org/pdf/2512.17250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17250v1', 'Accelerating Multi-modal LLM Gaming Performance via Input Prediction and Mishit Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Lin, Zixuan Sun, Sanhorn Chen, Xiaoyang Chen, Roy Zhao

**分类**: cs.AI

**发布日期**: 2025-12-19

**备注**: UIUC 25 Fall CS 498

---

## 💡 一句话要点

**提出基于输入预测和误差校正的多模态LLM游戏加速框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态LLM` `实时控制` `模型预测控制` `推测执行` `误差校正` `延迟优化` `机器人` `游戏AI`

## 📋 核心要点

1. 现有实时控制智能体受限于推理延迟，影响控制稳定性和性能。
2. 提出推测-校正框架，利用世界模型和MPC规划器生成动作队列，减少规划频率。
3. 实验表明，该方法显著降低推理次数和延迟，同时保持较好的控制性能。

## 📝 摘要（中文）

实时序列控制智能体常受限于推理延迟。即使是适度的单步规划延迟也会破坏控制的稳定性并降低整体性能。我们提出了一种推测-校正框架，该框架将推测执行的预测-验证理念应用于基于模型的TD-MPC2控制。在每个步骤中，预训练的世界模型和潜在空间MPC规划器生成一个短视界动作队列以及预测的潜在轨迹，允许智能体执行多个计划动作而无需立即重新规划。当新的观察结果到达时，系统会测量编码的真实潜在状态与排队的预测潜在状态之间的不匹配。对于小到中等的不匹配，一个轻量级的学习校正器将残差更新应用于推测动作，该动作是从离线重新规划教师中提炼出来的。对于较大的不匹配，智能体会安全地回退到完全重新规划并清除过时的动作队列。我们研究了一个门控双塔MLP校正器和一个时间Transformer校正器，以解决局部误差和系统漂移。在DMC Humanoid-Walk任务上的实验表明，我们的方法将规划推理次数从500次减少到282次，将端到端步延迟提高了25%，并保持了强大的控制性能，仅降低了7.1%的回报。消融实验结果表明，没有校正的推测执行在较长时间范围内是不可靠的，突出了不匹配感知校正对于鲁棒延迟降低的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决实时序列控制任务中，由于多模态大型语言模型（LLM）推理延迟导致的控制性能下降问题。现有方法通常依赖于每一步的即时规划，计算开销大，难以满足实时性要求，尤其是在复杂环境中。

**核心思路**：核心思路是采用“推测-校正”的策略，类似于CPU中的推测执行。智能体首先基于世界模型预测未来状态和动作序列，然后执行这些动作。当实际观测与预测不符时，通过轻量级的校正器对动作进行修正，避免完全重新规划，从而降低平均推理延迟。

**技术框架**：整体框架包含以下几个主要模块：1) 预训练的世界模型：用于预测未来状态；2) 潜在空间MPC规划器：生成短视界动作队列；3) 状态编码器：将观测编码为潜在状态；4) 误差检测器：计算实际潜在状态与预测潜在状态之间的不匹配程度；5) 校正器：根据不匹配程度对推测动作进行修正；6) 回退机制：当不匹配过大时，回退到完全重新规划。

**关键创新**：关键创新在于将推测执行的思想引入到基于模型的控制中，并提出了不匹配感知的校正机制。与传统的推测执行不同，该方法不是简单地丢弃错误的推测结果，而是尝试通过学习到的校正器来修正动作，从而更有效地利用计算资源。此外，论文还探索了不同的校正器结构（MLP和Transformer），以适应不同的误差模式。

**关键设计**：论文设计了两种校正器：门控双塔MLP校正器和时间Transformer校正器。MLP校正器用于处理局部误差，而Transformer校正器用于处理系统性漂移。校正器的训练采用离线蒸馏的方式，以重新规划的教师模型为目标。损失函数的设计需要平衡校正的精度和稳定性，避免过度校正导致控制不稳定。具体参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17250v1/sd-vllm.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17250v1/263a66ec-f63d-4057-b71f-790564ed66a7.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17250v1/speculation.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在DMC Humanoid-Walk任务中，将规划推理次数从500次减少到282次，端到端步延迟提高了25%，同时仅降低了7.1%的回报。消融实验验证了不匹配感知校正对于鲁棒延迟降低的必要性，表明单纯的推测执行在长时间范围内不可靠。

## 🎯 应用场景

该研究成果可应用于各种需要实时控制的场景，例如机器人导航、游戏AI、自动驾驶等。通过降低推理延迟，可以提高控制系统的响应速度和稳定性，从而改善用户体验和系统性能。此外，该方法还可以扩展到其他类型的模型和任务中，具有广泛的应用前景。

## 📄 摘要（原文）

> Real-time sequential control agents are often bottlenecked by inference latency. Even modest per-step planning delays can destabilize control and degrade overall performance. We propose a speculation-and-correction framework that adapts the predict-then-verify philosophy of speculative execution to model-based control with TD-MPC2. At each step, a pretrained world model and latent-space MPC planner generate a short-horizon action queue together with predicted latent rollouts, allowing the agent to execute multiple planned actions without immediate replanning. When a new observation arrives, the system measures the mismatch between the encoded real latent state and the queued predicted latent. For small to moderate mismatch, a lightweight learned corrector applies a residual update to the speculative action, distilled offline from a replanning teacher. For large mismatch, the agent safely falls back to full replanning and clears stale action queues. We study both a gated two-tower MLP corrector and a temporal Transformer corrector to address local errors and systematic drift. Experiments on the DMC Humanoid-Walk task show that our method reduces the number of planning inferences from 500 to 282, improves end-to-end step latency by 25 percent, and maintains strong control performance with only a 7.1 percent return reduction. Ablation results demonstrate that speculative execution without correction is unreliable over longer horizons, highlighting the necessity of mismatch-aware correction for robust latency reduction.

