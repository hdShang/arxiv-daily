---
layout: default
title: Lessons from Defending Gemini Against Indirect Prompt Injections
---

# Lessons from Defending Gemini Against Indirect Prompt Injections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14534" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14534v1</a>
  <a href="https://arxiv.org/pdf/2505.14534.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14534v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14534v1', 'Lessons from Defending Gemini Against Indirect Prompt Injections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chongyang Shi, Sharon Lin, Shuang Song, Jamie Hayes, Ilia Shumailov, Itay Yona, Juliette Pluto, Aneesh Pappu, Christopher A. Choquette-Choo, Milad Nasr, Chawin Sitawarin, Gena Gibson, Andreas Terzis, John "Four" Flynn

**分类**: cs.CR, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出对抗性评估框架以增强Gemini模型的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `对抗性攻击` `模型鲁棒性` `安全性评估` `Gemini模型` `深度学习` `数据处理` `智能助手`

## 📋 核心要点

1. 现有的Gemini模型在处理不可信数据时面临对手嵌入恶意指令的风险，可能导致数据处理错误。
2. 论文提出了一种对抗性评估框架，利用适应性攻击技术持续测试Gemini模型的鲁棒性。
3. 通过持续的评估，Gemini模型在抵御操控方面表现出显著提升，增强了其安全性和可靠性。

## 📝 摘要（中文）

Gemini模型越来越多地被用于代表用户执行任务，但某些工具需要访问不可信的数据，从而引入风险。对手可以在不可信数据中嵌入恶意指令，导致模型偏离用户期望并错误处理数据或权限。本文介绍了Google DeepMind对Gemini模型的对抗性鲁棒性评估方法，并总结了从中获得的主要经验教训。通过对Gemini进行持续的对抗性评估，本文展示了如何使模型更具抵御操控的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决Gemini模型在处理不可信数据时的对抗性脆弱性，现有方法未能有效防止对手的恶意指令嵌入。

**核心思路**：通过建立对抗性评估框架，持续测试Gemini模型的鲁棒性，及时发现并修复潜在的安全漏洞。

**技术框架**：整体架构包括对抗性评估模块、适应性攻击技术和模型反馈机制，形成闭环评估与改进流程。

**关键创新**：最重要的创新在于持续的对抗性评估方法，使得模型能够在多个版本中不断适应和增强，区别于传统的静态评估方法。

**关键设计**：在评估过程中，采用了多种适应性攻击技术，设置了特定的评估指标，以确保模型在不同版本间的鲁棒性提升。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果表明，通过对抗性评估框架，Gemini模型在面对复杂攻击时的鲁棒性显著提升，具体性能数据和提升幅度在论文中详细列出，显示出模型在多个版本间的持续改进。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化工具和数据处理系统，能够有效提升这些系统在面对不可信数据时的安全性和可靠性。未来，随着对抗性攻击技术的不断演进，该框架可能会成为评估和增强AI模型安全性的标准工具。

## 📄 摘要（原文）

> Gemini is increasingly used to perform tasks on behalf of users, where function-calling and tool-use capabilities enable the model to access user data. Some tools, however, require access to untrusted data introducing risk. Adversaries can embed malicious instructions in untrusted data which cause the model to deviate from the user's expectations and mishandle their data or permissions. In this report, we set out Google DeepMind's approach to evaluating the adversarial robustness of Gemini models and describe the main lessons learned from the process. We test how Gemini performs against a sophisticated adversary through an adversarial evaluation framework, which deploys a suite of adaptive attack techniques to run continuously against past, current, and future versions of Gemini. We describe how these ongoing evaluations directly help make Gemini more resilient against manipulation.

