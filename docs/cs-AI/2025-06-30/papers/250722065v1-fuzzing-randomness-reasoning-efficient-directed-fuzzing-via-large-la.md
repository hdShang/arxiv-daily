---
layout: default
title: "Fuzzing: Randomness? Reasoning! Efficient Directed Fuzzing via Large Language Models"
---

# Fuzzing: Randomness? Reasoning! Efficient Directed Fuzzing via Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.22065" class="toolbar-btn" target="_blank">📄 arXiv: 2507.22065v1</a>
  <a href="https://arxiv.org/pdf/2507.22065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.22065v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.22065v1', 'Fuzzing: Randomness? Reasoning! Efficient Directed Fuzzing via Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaotao Feng, Xiaogang Zhu, Kun Hu, Jincheng Wang, Yingjie Cao, Guang Gong, Jianfeng Pan

**分类**: cs.SE, cs.AI, cs.CR, cs.PL

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出RandLuzz以解决模糊测试中的随机性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模糊测试` `漏洞检测` `大型语言模型` `定向模糊测试` `软件安全` `自动化测试`

## 📋 核心要点

1. 现有模糊测试方法依赖随机性，导致效率低下，难以快速发现漏洞。
2. 本文提出RandLuzz，通过大型语言模型生成可达种子和特定变异器，减少随机性，提高模糊测试效率。
3. 实验表明，RandLuzz生成的种子使模糊测试器速度提升2.1倍至4.8倍，且在多个漏洞上实现快速暴露。

## 📝 摘要（中文）

模糊测试因其随机性在检测漏洞方面极为有效，但这种随机性显著降低了效率，导致需要耗费数天或数周才能发现漏洞。尽管定向模糊测试通过引导模糊测试向目标漏洞位置靠拢来减少随机性，但随机性仍然是定向模糊测试面临的挑战。为了解决这一问题，本文提出使用大型语言模型（LLMs）来消除种子中的随机性，并减少变异器中的随机性。RandLuzz结合了LLMs与定向模糊测试，生成可达种子和特定漏洞的变异器，从而提高了漏洞暴露的效率。实验结果表明，RandLuzz生成的种子使模糊测试器的速度提升范围为2.1倍至4.8倍，且在8个漏洞上，RandLuzz能够在60秒内暴露漏洞。

## 🔬 方法详解

**问题定义**：本文旨在解决模糊测试中的随机性问题，现有方法在生成种子和变异器时依赖随机性，导致效率低下，难以快速触发漏洞。

**核心思路**：通过利用大型语言模型（LLMs）的推理和代码生成能力，RandLuzz能够生成针对特定漏洞的可达种子和变异器，从而减少随机性，提高模糊测试的效率。

**技术框架**：RandLuzz的整体架构包括两个主要模块：种子生成模块和变异器构建模块。种子生成模块分析函数调用链或功能，指导LLMs生成可达种子；变异器构建模块则通过LLMs进行漏洞分析，获取漏洞原因和变异建议，生成特定的变异器代码。

**关键创新**：RandLuzz的创新在于将LLMs引入模糊测试中，利用其强大的推理能力来生成高质量的种子和变异器，这与传统模糊测试方法依赖随机生成的方式有本质区别。

**关键设计**：在种子生成过程中，RandLuzz通过分析目标函数的调用链来指导LLMs生成有效的种子；在变异器构建中，LLMs通过漏洞分析获取变异建议，确保生成的变异器能够针对特定漏洞进行有效的变异。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

RandLuzz在与四种最先进的定向模糊测试器（AFLGo、Beacon、WindRanger和SelectFuzz）比较中，生成的种子使模糊测试器的平均速度提升范围为2.1倍至4.8倍。在针对单个漏洞的评估中，RandLuzz实现了高达2.7倍的速度提升，并在8个漏洞上能够在60秒内成功暴露漏洞。

## 🎯 应用场景

RandLuzz的研究成果在软件测试、漏洞检测和安全性评估等领域具有广泛的应用潜力。通过提高模糊测试的效率，RandLuzz能够帮助开发者更快地发现和修复软件中的安全漏洞，从而提升软件的安全性和可靠性。未来，RandLuzz还可以与其他自动化测试工具结合，进一步增强软件测试的智能化水平。

## 📄 摘要（原文）

> Fuzzing is highly effective in detecting bugs due to the key contribution of randomness. However, randomness significantly reduces the efficiency of fuzzing, causing it to cost days or weeks to expose bugs. Even though directed fuzzing reduces randomness by guiding fuzzing towards target buggy locations, the dilemma of randomness still challenges directed fuzzers. Two critical components, which are seeds and mutators, contain randomness and are closely tied to the conditions required for triggering bugs. Therefore, to address the challenge of randomness, we propose to use large language models (LLMs) to remove the randomness in seeds and reduce the randomness in mutators. With their strong reasoning and code generation capabilities, LLMs can be used to generate reachable seeds that target pre-determined locations and to construct bug-specific mutators tailored for specific bugs. We propose RandLuzz, which integrates LLMs and directed fuzzing, to improve the quality of seeds and mutators, resulting in efficient bug exposure. RandLuzz analyzes function call chain or functionality to guide LLMs in generating reachable seeds. To construct bug-specific mutators, RandLuzz uses LLMs to perform bug analysis, obtaining information such as bug causes and mutation suggestions, which further help generate code that performs bug-specific mutations. We evaluate RandLuzz by comparing it with four state-of-the-art directed fuzzers, AFLGo, Beacon, WindRanger, and SelectFuzz. With RandLuzz-generated seeds, the fuzzers achieve an average speedup ranging from 2.1$\times$ to 4.8$\times$ compared to using widely-used initial seeds. Additionally, when evaluated on individual bugs, RandLuzz achieves up to a 2.7$\times$ speedup compared to the second-fastest exposure. On 8 bugs, RandLuzz can even expose them within 60 seconds.

