---
layout: default
title: MADRA: Multi-Agent Debate for Risk-Aware Embodied Planning
---

# MADRA: Multi-Agent Debate for Risk-Aware Embodied Planning

**arXiv**: [2511.21460v1](https://arxiv.org/abs/2511.21460) | [PDF](https://arxiv.org/pdf/2511.21460.pdf)

**作者**: Junjian Wang, Lidan Zhao, Xi Sheryl Zhang

---

## 💡 一句话要点

**提出MADRA多智能体辩论框架以解决具身AI任务规划中的安全风险问题**

**关键词**: `具身AI` `多智能体辩论` `风险感知规划` `安全评估` `训练免费框架` `基准数据集`

## 📋 核心要点

1. 现有方法存在计算成本高或过度拒绝安全指令的问题
2. 采用多智能体辩论和共识投票，无需训练即可提升安全评估
3. 在AI2-THOR和VirtualHome实验中，拒绝90%以上危险任务且安全任务拒绝率低

## 📄 摘要（原文）

> Ensuring the safety of embodied AI agents during task planning is critical for real-world deployment, especially in household environments where dangerous instructions pose significant risks. Existing methods often suffer from either high computational costs due to preference alignment training or over-rejection when using single-agent safety prompts. To address these limitations, we propose MADRA, a training-free Multi-Agent Debate Risk Assessment framework that leverages collective reasoning to enhance safety awareness without sacrificing task performance. MADRA employs multiple LLM-based agents to debate the safety of a given instruction, guided by a critical evaluator that scores responses based on logical soundness, risk identification, evidence quality, and clarity. Through iterative deliberation and consensus voting, MADRA significantly reduces false rejections while maintaining high sensitivity to dangerous tasks. Additionally, we introduce a hierarchical cognitive collaborative planning framework that integrates safety, memory, planning, and self-evolution mechanisms to improve task success rates through continuous learning. We also contribute SafeAware-VH, a benchmark dataset for safety-aware task planning in VirtualHome, containing 800 annotated instructions. Extensive experiments on AI2-THOR and VirtualHome demonstrate that our approach achieves over 90% rejection of unsafe tasks while ensuring that safe-task rejection is low, outperforming existing methods in both safety and execution efficiency. Our work provides a scalable, model-agnostic solution for building trustworthy embodied agents.

