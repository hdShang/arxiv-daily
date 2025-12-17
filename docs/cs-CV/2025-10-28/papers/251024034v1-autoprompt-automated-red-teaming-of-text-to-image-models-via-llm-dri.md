---
layout: default
title: AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts
---

# AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts

**arXiv**: [2510.24034v1](https://arxiv.org/abs/2510.24034) | [PDF](https://arxiv.org/pdf/2510.24034.pdf)

**作者**: Yufan Liu, Wanqian Zhang, Huashan Chen, Lin Wang, Xiaojun Jia, Zheng Lin, Weiping Wang

---

## 💡 一句话要点

**提出AutoPrompt框架，利用LLM生成可读对抗提示以黑盒测试文本到图像模型安全漏洞**

**关键词**: `文本到图像模型` `对抗提示` `红队测试` `大语言模型` `黑盒攻击` `零样本迁移`

## 📋 核心要点

1. 问题：文本到图像模型易受对抗提示攻击，现有红队方法需白盒访问且效率低
2. 方法：采用交替优化微调流程，结合双规避策略绕过过滤器和黑名单
3. 效果：实验显示高红队性能、强零样本迁移性，可攻击商业API如Leonardo.Ai

## 📄 摘要（原文）

> Despite rapid advancements in text-to-image (T2I) models, their safety
> mechanisms are vulnerable to adversarial prompts, which maliciously generate
> unsafe images. Current red-teaming methods for proactively assessing such
> vulnerabilities usually require white-box access to T2I models, and rely on
> inefficient per-prompt optimization, as well as inevitably generate
> semantically meaningless prompts easily blocked by filters. In this paper, we
> propose APT (AutoPrompT), a black-box framework that leverages large language
> models (LLMs) to automatically generate human-readable adversarial suffixes for
> benign prompts. We first introduce an alternating optimization-finetuning
> pipeline between adversarial suffix optimization and fine-tuning the LLM
> utilizing the optimized suffix. Furthermore, we integrates a dual-evasion
> strategy in optimization phase, enabling the bypass of both perplexity-based
> filter and blacklist word filter: (1) we constrain the LLM generating
> human-readable prompts through an auxiliary LLM perplexity scoring, which
> starkly contrasts with prior token-level gibberish, and (2) we also introduce
> banned-token penalties to suppress the explicit generation of banned-tokens in
> blacklist. Extensive experiments demonstrate the excellent red-teaming
> performance of our human-readable, filter-resistant adversarial prompts, as
> well as superior zero-shot transferability which enables instant adaptation to
> unseen prompts and exposes critical vulnerabilities even in commercial APIs
> (e.g., Leonardo.Ai.).

