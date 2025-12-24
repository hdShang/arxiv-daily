---
layout: default
title: OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning
---

# OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08617" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08617v2</a>
  <a href="https://arxiv.org/pdf/2505.08617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08617v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08617v2', 'OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaochen Su, Linjie Li, Mingyang Song, Yunzhuo Hao, Zhengyuan Yang, Jun Zhang, Guanjie Chen, Jiawei Gu, Juntao Li, Xiaoye Qu, Yu Cheng

**分类**: cs.CV

**发布日期**: 2025-05-13 (更新: 2025-07-09)

**备注**: Work in progress

---

## 💡 一句话要点

**提出OpenThinkIMG以解决视觉工具增强学习的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉工具增强` `强化学习` `视觉推理` `多模态学习` `开源框架`

## 📋 核心要点

1. 当前大型视觉语言模型在动态工具调用方面的适应性不足，缺乏有效的训练框架。
2. 提出OpenThinkIMG框架，结合标准化视觉工具接口和V-ToolRL强化学习方法，提升工具使用策略的学习能力。
3. 实验结果显示，基于V-ToolRL训练的代理在图表推理任务上超越了传统的监督学习基线，提升幅度显著。

## 📝 摘要（中文）

人类能够灵活利用交互式视觉认知进行复杂问题解决，但使大型视觉语言模型（LVLMs）学习类似的适应性行为仍然面临挑战。当前缺乏标准化基础设施，限制了多样化工具的集成、丰富交互数据的生成以及有效训练强健代理的能力。为此，我们提出OpenThinkIMG，这是第一个开源的全面端到端框架，旨在增强LVLMs的工具使用能力。该框架提供标准化的视觉工具接口、可扩展的轨迹生成和灵活的训练环境。此外，我们提出了一种新颖的强化学习框架V-ToolRL，以训练LVLMs学习动态工具调用的适应性策略。通过在复杂的图表推理任务上进行实证验证，我们的RL训练代理显著超越了基于监督微调的对比模型，展示了OpenThinkIMG在动态视觉推理中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型视觉语言模型在动态工具调用中的适应性不足问题。现有方法主要依赖于静态演示的监督微调，导致策略泛化能力有限。

**核心思路**：提出OpenThinkIMG框架，通过标准化的视觉工具接口和V-ToolRL强化学习方法，帮助LVLMs自主发现最佳工具使用策略，从而提高任务成功率。

**技术框架**：OpenThinkIMG框架包括三个主要模块：标准化视觉工具接口、可扩展的轨迹生成模块和灵活的训练环境。V-ToolRL作为核心算法，直接通过工具交互反馈优化策略。

**关键创新**：V-ToolRL是本研究的核心创新，允许LVLMs在动态环境中自主学习工具使用策略，与传统的监督学习方法相比，具有更高的灵活性和适应性。

**关键设计**：在V-ToolRL中，设计了特定的损失函数以优化任务成功率，并采用了Qwen2-VL-2B作为基础模型，确保了训练的有效性和效率。

## 📊 实验亮点

实验结果表明，基于V-ToolRL训练的代理在图表推理任务上比监督微调初始化的模型提高了28.83分，且超越了现有的监督工具学习基线，如Taco和CogCom，平均提升12.7分。此外，该模型还在准确性上超越了GPT-4.1，提升了8.68分。

## 🎯 应用场景

OpenThinkIMG框架可广泛应用于需要视觉推理和工具交互的领域，如智能助手、数据分析和教育技术等。其灵活的设计使得AI代理能够在动态环境中更好地理解和处理视觉信息，提升用户体验和决策支持能力。

## 📄 摘要（原文）

> While humans can flexibly leverage interactive visual cognition for complex problem-solving, enabling Large Vision-Language Models (LVLMs) to learn similarly adaptive behaviors with visual tools remains challenging. A significant hurdle is the current lack of standardized infrastructure, which hinders integrating diverse tools, generating rich interaction data, and training robust agents effectively. To address these gaps, we introduce OpenThinkIMG, the first open-source, comprehensive end-to-end framework for tool-augmented LVLMs. It features standardized vision tool interfaces, scalable trajectory generation for policy initialization, and a flexible training environment. Furthermore, considering supervised fine-tuning (SFT) on static demonstrations offers limited policy generalization for dynamic tool invocation, we propose a novel reinforcement learning (RL) framework V-ToolRL to train LVLMs to learn adaptive policies for invoking external vision tools. V-ToolRL enables LVLMs to autonomously discover optimal tool-usage strategies by directly optimizing for task success using feedback from tool interactions. We empirically validate V-ToolRL on challenging chart reasoning tasks. Our RL-trained agent, built upon a Qwen2-VL-2B, significantly outperforms its SFT-initialized counterpart (+28.83 points) and surpasses established supervised tool-learning baselines like Taco and CogCom by an average of +12.7 points. Notably, it also surpasses prominent closed-source models like GPT-4.1 by +8.68 accuracy points. We hope OpenThinkIMG can serve as a foundational framework for advancing dynamic, tool-augmented visual reasoning, helping the community develop AI agents that can genuinely "think with images".

