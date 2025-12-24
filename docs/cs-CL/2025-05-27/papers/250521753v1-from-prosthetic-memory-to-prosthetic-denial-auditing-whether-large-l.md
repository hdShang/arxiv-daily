---
layout: default
title: "From prosthetic memory to prosthetic denial: Auditing whether large language models are prone to mass atrocity denialism"
---

# From prosthetic memory to prosthetic denial: Auditing whether large language models are prone to mass atrocity denialism

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21753" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21753v1</a>
  <a href="https://arxiv.org/pdf/2505.21753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21753v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21753v1', 'From prosthetic memory to prosthetic denial: Auditing whether large language models are prone to mass atrocity denialism')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roberto Ulloa, Eve M. Zucker, Daniel Bultmann, David J. Simon, Mykola Makhortykh

**分类**: cs.CY, cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**审计大型语言模型对历史记忆的影响与否定主义风险**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `历史记忆` `否认主义` `数字记忆` `伦理问题` `暴行研究` `比较审计`

## 📋 核心要点

1. 现有大型语言模型在处理历史事件时，可能会导致对某些暴行的否认或扭曲，影响历史记忆的完整性。
2. 本研究通过比较审计不同LLMs的输出，探讨其在历史记忆传递中的作用及潜在风险。
3. 实验结果表明，LLMs在处理广泛记录的历史事件时表现良好，但在较少被关注的事件中存在显著的否认主义倾向。

## 📝 摘要（中文）

大型语言模型（LLMs）的普及可能影响历史叙事的传播与认知。本研究探讨了LLMs在大规模暴行记忆表现上的影响，分析其是否助长了“假肢否认”，即对暴行记忆的抹去或扭曲。我们通过对五种LLMs（Claude、GPT、Llama、Mixtral和Gemini）进行比较审计，针对四个历史案例（霍洛多莫尔、 Holocaust、柬埔寨大屠杀和卢旺达图西人种族灭绝）提出了相关问题。结果显示，尽管LLMs在广泛记录的事件中表现准确，但在较少被记录的事件中存在显著的不一致性和否认主义倾向，强调了训练数据可用性对记忆完整性的影响。我们得出结论，LLMs在扩展假肢记忆概念的同时，其不加以审查的使用可能会加剧历史否认主义，带来数字记忆保存的伦理问题。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在历史事件叙述中可能引发的否认主义问题，现有方法在处理较少记录的事件时存在显著不足。

**核心思路**：通过比较审计五种不同的LLMs，分析其在处理历史暴行记忆时的表现，探讨其对假肢记忆和否认主义的影响。

**技术框架**：研究分为几个主要阶段：选择历史案例、设计针对性问题、收集LLMs的响应、分析输出结果及其一致性。

**关键创新**：本研究的创新在于系统性地审计不同LLMs在处理历史记忆时的表现，揭示了它们在不同事件上的响应差异，特别是在较少被记录的事件中。

**关键设计**：在实验中，针对每个历史案例设计了特定的问题，使用了多种语言（如英语、乌克兰语、德语、法语和高棉语）进行测试，以确保对不同文化背景的适应性。实验还考虑了训练数据的可用性对模型输出的影响。

## 📊 实验亮点

实验结果显示，LLMs在处理广泛记录的事件（如Holocaust）时，准确率较高，而在较少被关注的事件（如柬埔寨大屠杀）中，存在显著的不一致性和否认主义倾向。这一发现强调了训练数据的可用性对模型输出的影响。

## 🎯 应用场景

该研究的潜在应用领域包括历史教育、数字记忆保存和AI伦理研究。通过理解LLMs在历史叙事中的作用，可以为教育工作者和政策制定者提供指导，确保历史记忆的准确传递，避免技术对历史认知的负面影响。

## 📄 摘要（原文）

> The proliferation of large language models (LLMs) can influence how historical narratives are disseminated and perceived. This study explores the implications of LLMs' responses on the representation of mass atrocity memory, examining whether generative AI systems contribute to prosthetic memory, i.e., mediated experiences of historical events, or to what we term "prosthetic denial," the AI-mediated erasure or distortion of atrocity memories. We argue that LLMs function as interfaces that can elicit prosthetic memories and, therefore, act as experiential sites for memory transmission, but also introduce risks of denialism, particularly when their outputs align with contested or revisionist narratives. To empirically assess these risks, we conducted a comparative audit of five LLMs (Claude, GPT, Llama, Mixtral, and Gemini) across four historical case studies: the Holodomor, the Holocaust, the Cambodian Genocide, and the genocide against the Tutsis in Rwanda. Each model was prompted with questions addressing common denialist claims in English and an alternative language relevant to each case (Ukrainian, German, Khmer, and French). Our findings reveal that while LLMs generally produce accurate responses for widely documented events like the Holocaust, significant inconsistencies and susceptibility to denialist framings are observed for more underrepresented cases like the Cambodian Genocide. The disparities highlight the influence of training data availability and the probabilistic nature of LLM responses on memory integrity. We conclude that while LLMs extend the concept of prosthetic memory, their unmoderated use risks reinforcing historical denialism, raising ethical concerns for (digital) memory preservation, and potentially challenging the advantageous role of technology associated with the original values of prosthetic memory.

