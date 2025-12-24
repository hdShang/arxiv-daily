---
layout: default
title: "AutoCode: LLMs as Problem Setters for Competitive Programming"
---

# AutoCode: LLMs as Problem Setters for Competitive Programming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.12803" class="toolbar-btn" target="_blank">📄 arXiv: 2510.12803v1</a>
  <a href="https://arxiv.org/pdf/2510.12803.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.12803v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.12803v1', 'AutoCode: LLMs as Problem Setters for Competitive Programming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shang Zhou, Zihan Zheng, Kaiyuan Liu, Zeyu Shen, Zerui Cheng, Zexing Chen, Hansen He, Jianzhu Yao, Huanzhi Mao, Qiuyang Mang, Tianfu Fu, Beichen Li, Dongruixuan Li, Wenhao Chai, Zhuang Liu, Aleksandra Korolova, Peter Henderson, Natasha Jaques, Pramod Viswanath, Saining Xie, Jingbo Shang

**分类**: cs.SE, cs.AI, cs.CL, cs.PL

**发布日期**: 2025-09-29

**备注**: Project page: https://livecodebenchpro.com/projects/autocode/overview

---

## 💡 一句话要点

**AutoCode：利用大型语言模型自动生成竞赛级编程题目**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `编程竞赛` `自动出题` `测试用例生成` `多轮验证`

## 📋 核心要点

1. 现有竞赛编程题目生成方法难以兼顾约束条件、算法针对性和难度校准，对出题者要求极高。
2. AutoCode利用大型语言模型，通过多轮验证生成高质量题目描述和测试用例，并能生成参考和暴力解法。
3. 实验表明，AutoCode生成的测试套件与官方判定的结果一致性接近99%，显著优于现有方法。

## 📝 摘要（中文）

编写竞赛编程题目极具挑战性。出题者必须设定约束条件、输入分布和排除作弊的边界情况；针对特定算法（如最大流、动态规划、数据结构）；并校准难度，使其超出大多数参赛者的能力范围。我们认为这非常适合测试通用大型语言模型的能力，并研究它们是否能可靠地完成这项任务。我们介绍了AutoCode，它使用多轮验证来生成竞赛级的题目描述和测试用例。在保留问题上，AutoCode测试套件与官方判定的结果一致性接近99%，与当前最先进的方法（如HardTests，一致性低于81%）相比，有了显著提高。此外，从随机种子问题开始，AutoCode可以创建具有参考解决方案和暴力破解解决方案的新变体。通过交叉验证这些生成的解决方案与测试用例，我们可以进一步过滤掉格式错误的问题。我们的系统确保了高正确性，并经过了人类专家的验证。AutoCode成功地生成了由Grandmaster级别（前0.3%）的竞赛程序员判断为竞赛质量的新问题。

## 🔬 方法详解

**问题定义**：论文旨在解决自动生成高质量、竞赛级别的编程题目的问题。现有方法，如HardTests，在生成测试用例时，与官方判定的结果一致性较低，无法保证题目的有效性和可靠性。人工出题成本高昂，且需要出题者具备深厚的算法功底和丰富的竞赛经验。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）的强大生成能力和理解能力，自动生成题目描述、测试用例以及参考解法。通过多轮验证和交叉验证，筛选出高质量的题目，并确保其难度和区分度符合竞赛要求。

**技术框架**：AutoCode系统主要包含以下几个阶段：1) 题目生成：利用LLM生成初始的题目描述；2) 测试用例生成：利用LLM生成测试用例，包括正常情况和边界情况；3) 解法生成：利用LLM生成参考解法和暴力解法；4) 验证与筛选：通过交叉验证测试用例和解法，筛选出高质量的题目。人类专家会对最终生成的题目进行评估和确认。

**关键创新**：AutoCode的关键创新在于利用LLM进行多轮验证和交叉验证，从而有效地筛选出高质量的题目。与现有方法相比，AutoCode能够生成更复杂、更具挑战性的题目，并且能够保证题目的正确性和可靠性。此外，AutoCode还能够自动生成参考解法和暴力解法，方便出题者进行验证和评估。

**关键设计**：AutoCode在题目生成阶段，会使用特定的prompt来引导LLM生成符合竞赛要求的题目描述。在测试用例生成阶段，会考虑各种边界情况和特殊情况，以确保题目的鲁棒性。在验证与筛选阶段，会使用多种指标来评估题目的质量，例如测试用例的覆盖率、解法的正确率等。具体的参数设置和损失函数细节在论文中未详细描述，属于未知信息。

## 📊 实验亮点

AutoCode在保留问题上，测试套件与官方判定的结果一致性接近99%，显著优于当前最先进的方法HardTests（一致性低于81%）。由Grandmaster级别（前0.3%）的竞赛程序员判断，AutoCode成功生成了竞赛质量的新问题，证明了其生成高质量竞赛题目的能力。

## 🎯 应用场景

AutoCode可应用于各种编程竞赛和在线评测系统，降低出题成本，提高题目质量和多样性。它还可以用于教育领域，辅助教师生成练习题和考试题，帮助学生提高编程能力。此外，该技术还可用于自动化测试和软件质量评估，生成更全面的测试用例，提高软件的可靠性。

## 📄 摘要（原文）

> Writing competitive programming problems is exacting. Authors must: set constraints, input distributions, and edge cases that rule out shortcuts; target specific algorithms (e.g., max-flow, dynamic programming, data structures); and calibrate complexity beyond the reach of most competitors. We argue that this makes for an ideal test of general large language model capabilities and study whether they can do this reliably. We introduce AutoCode, which uses multiple rounds of validation to yield competition-grade problem statements and test cases. On held-out problems, AutoCode test suites approach 99% consistency with official judgments, a significant improvement over current state-of-the-art methods like HardTests, which achieve less than 81%. Furthermore, starting with a random seed problem, AutoCode can create novel variants with reference and brute-force solutions. By cross-verifying these generated solutions against test cases, we can further filter out malformed problems. Our system ensures high correctness, as verified by human experts. AutoCode successfully produces novel problems judged by Grandmaster-level (top 0.3%) competitive programmers to be of contest quality.

