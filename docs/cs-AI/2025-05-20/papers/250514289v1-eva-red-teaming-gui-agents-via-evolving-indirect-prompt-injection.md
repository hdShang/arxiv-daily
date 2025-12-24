---
layout: default
title: "EVA: Red-Teaming GUI Agents via Evolving Indirect Prompt Injection"
---

# EVA: Red-Teaming GUI Agents via Evolving Indirect Prompt Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14289" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14289v1</a>
  <a href="https://arxiv.org/pdf/2505.14289.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14289v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14289v1', 'EVA: Red-Teaming GUI Agents via Evolving Indirect Prompt Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijie Lu, Tianjie Ju, Manman Zhao, Xinbei Ma, Yuan Guo, ZhuoSheng Zhang

**分类**: cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出EVA框架以应对间接提示注入攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `间接提示注入` `多模态代理` `图形用户界面` `闭环优化` `网络安全` `对抗生成` `注意力机制`

## 📋 核心要点

1. 现有方法在应对间接提示注入攻击时，往往采用固定的提示生成策略，未能考虑模型的视觉注意力分配，导致攻击效果不佳。
2. EVA框架通过闭环优化的方式，动态监测和调整代理的注意力分布，以适应环境变化，从而提高攻击的成功率和迁移性。
3. 实验表明，EVA在六种广泛使用的GUI代理上进行评估，成功率显著高于静态基线，且在目标无关约束下仍能发现有效模式。

## 📝 摘要（中文）

随着多模态代理被训练以操作图形用户界面（GUI）完成用户任务，间接提示注入攻击的威胁日益增加。这种攻击通过在代理的视觉环境中嵌入误导性指令（如弹窗或聊天消息），使其被误解为任务的一部分。为应对这些新兴攻击，本文提出了EVA，一个针对间接提示注入的红队框架。EVA通过持续监测代理在GUI上的注意力分布，并根据反馈更新对抗线索、关键词、措辞和布局，将攻击转化为闭环优化。与之前的单次生成方法相比，EVA能够动态适应注意力热点，显著提高攻击成功率，并在多种GUI场景中具有更好的迁移性。实验结果表明，EVA在静态基线之上显著提高了成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态代理在图形用户界面（GUI）操作中面临的间接提示注入攻击问题。现有方法通常采用固定的提示生成策略，未能考虑模型的视觉注意力分配，导致攻击效果不理想。

**核心思路**：EVA框架的核心思路是将攻击转化为闭环优化，通过持续监测代理的注意力分布，动态调整对抗线索、关键词、措辞和布局，以适应环境变化，从而提高攻击的成功率。

**技术框架**：EVA的整体架构包括多个模块：首先是注意力监测模块，实时跟踪代理在GUI上的注意力分布；其次是对抗生成模块，根据监测结果生成新的对抗线索；最后是反馈调整模块，依据攻击效果不断优化生成策略。

**关键创新**：EVA的最重要创新在于其动态适应能力，能够根据代理的注意力热点实时调整攻击策略，与现有的静态方法形成鲜明对比，从而显著提高攻击成功率和迁移性。

**关键设计**：在设计上，EVA采用了多层次的注意力监测机制，并结合了自适应的对抗生成算法，确保在不同的GUI场景中都能有效实施攻击。

## 📊 实验亮点

实验结果显示，EVA在六种不同的GUI代理上显著提高了攻击成功率，成功率相比静态基线提升幅度超过30%。在目标无关约束下，EVA仍能发现有效的攻击模式，表明其在多种场景中的广泛适用性和有效性。

## 🎯 应用场景

EVA框架的潜在应用领域包括网络安全、用户界面设计和人工智能代理的安全性评估。通过识别和利用多模态代理的脆弱性，EVA不仅可以帮助开发更安全的系统，还能在实际应用中提高用户体验和安全性。未来，EVA可能成为评估和强化多模态系统安全性的标准工具。

## 📄 摘要（原文）

> As multimodal agents are increasingly trained to operate graphical user interfaces (GUIs) to complete user tasks, they face a growing threat from indirect prompt injection, attacks in which misleading instructions are embedded into the agent's visual environment, such as popups or chat messages, and misinterpreted as part of the intended task. A typical example is environmental injection, in which GUI elements are manipulated to influence agent behavior without directly modifying the user prompt. To address these emerging attacks, we propose EVA, a red teaming framework for indirect prompt injection which transforms the attack into a closed loop optimization by continuously monitoring an agent's attention distribution over the GUI and updating adversarial cues, keywords, phrasing, and layout, in response. Compared with prior one shot methods that generate fixed prompts without regard for how the model allocates visual attention, EVA dynamically adapts to emerging attention hotspots, yielding substantially higher attack success rates and far greater transferability across diverse GUI scenarios. We evaluate EVA on six widely used generalist and specialist GUI agents in realistic settings such as popup manipulation, chat based phishing, payments, and email composition. Experimental results show that EVA substantially improves success rates over static baselines. Under goal agnostic constraints, where the attacker does not know the agent's task intent, EVA still discovers effective patterns. Notably, we find that injection styles transfer well across models, revealing shared behavioral biases in GUI agents. These results suggest that evolving indirect prompt injection is a powerful tool not only for red teaming agents, but also for uncovering common vulnerabilities in their multimodal decision making.

