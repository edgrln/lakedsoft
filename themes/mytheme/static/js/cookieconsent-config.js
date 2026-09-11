// Config for vanilla-cookieconsent (https://github.com/orestbida/cookieconsent),
// loaded as an ES module from the CDN by both base.html (blog theme) and
// landing.html. The theming (--cc-* variables, .cc--darkmode, .pm__* etc.)
// lives in each of those templates' own inline <style> and matches this
// library's class names exactly - see CLAUDE.md.
//
// Wired to Google Consent Mode v2: base.html/landing.html set
// 'analytics_storage' etc. to 'denied' by default before GTM loads: this
// file grants it once the visitor accepts the "analytics" category, via
// onFirstConsent/onChange below.
//
// Single-language site (Russian) - this used to detect the visitor's
// language from a /fr/, /de/, /es/ URL prefix and serve one of four
// translation bundles; now there's only ever one. See CLAUDE.md
// "Multi-language content" history if the site needs another language again.
import * as CookieConsent from 'https://cdn.jsdelivr.net/npm/vanilla-cookieconsent@3/dist/cookieconsent.esm.js';

function updateGoogleConsent() {
    if (typeof window.gtag !== 'function') return;
    var granted = CookieConsent.acceptedCategory('analytics');
    window.gtag('consent', 'update', {
        analytics_storage: granted ? 'granted' : 'denied',
    });
}

CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: 'box',
            position: 'bottom left',
            equalWeightButtons: true,
            flipButtons: false,
        },
        preferencesModal: {
            layout: 'box',
            equalWeightButtons: true,
            flipButtons: false,
        },
    },
    categories: {
        necessary: {
            readOnly: true,
        },
        analytics: {},
    },
    language: {
        default: 'ru',
        translations: {
            ru: {
                consentModal: {
                    title: 'Мы используем cookie',
                    description: 'Мы используем cookie, чтобы понимать, как посетители используют сайт. Вы можете принять все, отклонить необязательные или настроить выбор.',
                    acceptAllBtn: 'Принять все',
                    acceptNecessaryBtn: 'Отклонить все',
                    showPreferencesBtn: 'Настроить',
                    footer: '<a href="/blog/cookie-policy/">Политика cookie</a>',
                },
                preferencesModal: {
                    title: 'Настройки cookie',
                    acceptAllBtn: 'Принять все',
                    acceptNecessaryBtn: 'Отклонить все',
                    savePreferencesBtn: 'Сохранить настройки',
                    closeIconLabel: 'Закрыть',
                    sections: [
                        {
                            title: 'Строго необходимые',
                            description: 'Нужны для корректной работы сайта. Отключить нельзя.',
                            linkedCategory: 'necessary',
                        },
                        {
                            title: 'Аналитика',
                            description: 'Помогает понять, как посетители используют сайт (Google Analytics через Google Tag Manager), чтобы мы могли его улучшать.',
                            linkedCategory: 'analytics',
                        },
                    ],
                },
            },
        },
    },
    onFirstConsent: updateGoogleConsent,
    onChange: updateGoogleConsent,
});
